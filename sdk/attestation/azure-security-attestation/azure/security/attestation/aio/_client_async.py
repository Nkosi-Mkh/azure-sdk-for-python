# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------
from typing import Dict, List, Any, TYPE_CHECKING, Tuple

import json
from threading import Lock
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.exceptions import raise_with_traceback

from .._generated.aio import AzureAttestationRestClient
from .._generated.models import (
    AttestationResult as GeneratedAttestationResult,
    RuntimeData,
    InitTimeData,
    DataType,
    AttestSgxEnclaveRequest,
    AttestOpenEnclaveRequest,
)
from .._configuration import AttestationClientConfiguration
from .._models import AttestationSigner, AttestationToken, AttestationResult
from .._common import merge_validation_args

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports

    from azure.core.credentials_async import AsyncTokenCredential


class AttestationClient(object):
    # pylint: disable=line-too-long, protected-access
    """Provides access to the Attestation family of APIs for trusted environment attestation.

    :param credential: Credentials for the caller used to interact with the service.
    :type credential: :class:`~azure.core.credentials_async.AsyncTokenCredential`
    :param str endpoint: The attestation instance base URI, for example https://mytenant.attest.azure.net.
    :keyword bool validate_token: If True, validate the token, otherwise return the token unvalidated.
    :keyword validation_callback: Function callback to allow clients to perform custom validation of the token.
        if the token is invalid, the `validation_callback` function should throw
        an exception.
    :paramtype validation_callback: ~typing.Callable[[~azure.security.attestation.AttestationToken, ~azure.security.attestation.AttestationSigner], None]
    :keyword bool validate_signature: If True, validate the signature of the token being validated.
    :keyword bool validate_expiration: If True, validate the expiration time of the token being validated.
    :keyword str issuer: Expected issuer, used if `validate_issuer` is true.
    :keyword float validation_slack: Slack time for validation - tolerance applied
        to help account for clock drift between the issuer and the current machine.
    :keyword bool validate_issuer: If True, validate that the issuer of the token matches the expected issuer.
    :keyword bool validate_not_before_time: If true, validate the "Not Before" time in the token.

    .. tip::
        The `validate_token`, `validation_callback`, `validate_signature`,
        `validate_expiration`, `validate_not_before_time`, `validate_issuer`, and
        `issuer` keyword arguments are default values applied to each API call within
        the :py:class:`AttestationClient` class. These values can be
        overridden on individual API calls as needed.

    For additional client creation configuration options, please see `Python Request
    Options <https://aka.ms/azsdk/python/options>`_.

    """

    def __init__(
        self, endpoint: str, credential: "AsyncTokenCredential", **kwargs: Any
    ) -> None:
        if not credential:
            raise ValueError("Missing credential.")
        self._config = AttestationClientConfiguration(**kwargs)
        self._client = AzureAttestationRestClient(credential, endpoint, **kwargs)
        self._statelock = Lock()
        self._signing_certificates = None

    @distributed_trace_async
    async def get_open_id_metadata(self, **kwargs: Any) -> Dict[str, Any]:
        """Retrieves the OpenID metadata configuration document for this attestation instance.

        The metadata configuration document is defined in the `OpenID Connect
        Discovery <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfigurationResponse>`_
        specification.

        The attestation service currently returns the following fields:

        * issuer
        * jwks_uri
        * claims_supported

        :return: OpenID metadata configuration
        :rtype: Dict[str, Any]
        """
        return await self._client.metadata_configuration.get(**kwargs)

    @distributed_trace_async
    async def get_signing_certificates(self, **kwargs: Any) -> List[AttestationSigner]:
        """Returns the set of signing certificates used to sign attestation tokens.

        :return: A list of :class:`azure.security.attestation.AttestationSigner` objects.
        :rtype: list[~azure.security.attestation.AttestationSigner]

        For additional request configuration options, please see `Python Request
        Options <https://aka.ms/azsdk/python/options>`_.

        """
        signing_certificates = await self._client.signing_certificates.get(**kwargs)
        signers = []
        for key in signing_certificates.keys:
            signers.append(AttestationSigner._from_generated(key))
        return signers

    @distributed_trace_async
    async def attest_sgx_enclave(
        self,
        quote: bytes,
        *,
        inittime_json: bytes = None,
        inittime_data: bytes = None,
        runtime_json: bytes = None,
        runtime_data: bytes = None,
        **kwargs: Any
    ) -> Tuple[AttestationResult, AttestationToken]:
        """Attests the validity of an SGX quote.

        :param bytes quote: An SGX quote generated from an Intel(tm) SGX enclave
        :keyword bytes inittime_data: Data presented at the time that the SGX
            enclave was initialized.
        :keyword bytes inittime_json: Data presented at the time that the SGX
            enclave was initialized, JSON encoded.
        :keyword bytes runtime_data: Data presented at the time that the open_enclave
            report was created.
        :keyword bytes runtime_json: Data presented at the time that the open_enclave
            report was created. JSON Encoded.
        :keyword str draft_policy: "draft" or "experimental" policy to be used with
            this attestation request. If this parameter is provided, then this
            policy document will be used for the attestation request.
            This allows a caller to test various policy documents against actual data
            before applying the policy document via the set_policy API
        :keyword bool validate_token: If True, validate the token, otherwise return the token unvalidated.
        :keyword validation_callback: Function callback to allow clients to perform custom validation of the token.
            if the token is invalid, the `validation_callback` function should throw
            an exception.
        :paramtype validation_callback: ~typing.Callable[[~azure.security.attestation.AttestationToken, ~azure.security.attestation.AttestationSigner], None]
        :keyword bool validate_signature: If True, validate the signature of the token being validated.
        :keyword bool validate_expiration: If True, validate the expiration time of the token being validated.
        :keyword str issuer: Expected issuer, used if `validate_issuer` is true.
        :keyword float validation_slack: Slack time for validation - tolerance applied
            to help account for clock drift between the issuer and the current machine.
        :keyword bool validate_issuer: If True, validate that the issuer of the token matches the expected issuer.
        :keyword bool validate_not_before_time: If true, validate the "Not Before" time in the token.

        :return: :class:`AttestationResult` containing the claims in the returned attestation token.
        :rtype: Tuple[~azure.security.attestation.AttestationResult, ~azure.security.attestation.AttestationToken]

        .. note::
            Note that if the `draft_policy` parameter is provided, the resulting
            attestation token will be an unsecured attestation token.

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_attest_enclave_async.py
                :start-after: [START attest_sgx_enclave_shared]
                :end-before: [END attest_sgx_enclave_shared]
                :language: python
                :dedent: 8
                :caption: Attesting an SGX Enclave

        For additional request configuration options, please see `Python Request
        Options <https://aka.ms/azsdk/python/options>`_.

        """

        if inittime_json and inittime_data:
            raise ValueError("Cannot provide both inittime_json and inittime_data.")
        if runtime_json and runtime_data:
            raise ValueError("Cannot provide both runtime_data and runtime_json.")

        # If the input was JSON, make sure that it's valid JSON before sending it
        # to the service.
        if inittime_json:
            try:
                json.loads(inittime_json)
            except json.JSONDecodeError:
                raise_with_traceback(ValueError, "Content must be valid JSON.")

        if runtime_json:
            try:
                json.loads(runtime_json)
            except json.JSONDecodeError:
                raise_with_traceback(ValueError, "Content must be valid JSON.")

        # Now create the RuntimeData object to be sent to the service.
        runtime = None
        if runtime_data:
            runtime = RuntimeData(data=runtime_data, data_type=DataType.BINARY)

        if runtime_json:
            runtime = RuntimeData(data=runtime_json, data_type=DataType.JSON)

        # And the InitTimeData object to be sent to the service.
        inittime = None
        if inittime_data:
            inittime = InitTimeData(data=inittime_data, data_type=DataType.BINARY)
        if inittime_json:
            inittime = InitTimeData(data=inittime_data, data_type=DataType.JSON)

        request = AttestSgxEnclaveRequest(
            quote=quote,
            init_time_data=inittime,
            runtime_data=runtime,
            draft_policy_for_attestation=kwargs.pop("draft_policy", None),
        )
        # Merge our existing config options with the options for this API call.
        # Note that this must be done before calling into the implementation
        # layer because the implementation layer doesn't like keyword args that
        # it doesn't expect :(.
        options = merge_validation_args(self._config._kwargs, kwargs)

        result = await self._client.attestation.attest_sgx_enclave(request, **kwargs)
        token = AttestationToken(
            token=result.token, body_type=GeneratedAttestationResult
        )

        if options.get("validate_token", True):
            token._validate_token(await self._get_signers(**kwargs), **options)
        return (
            AttestationResult._from_generated(token._get_body()),
            token,
        )

    @distributed_trace_async
    async def attest_open_enclave(
        self,
        report: bytes,
        *,
        inittime_json: bytes = None,
        inittime_data: bytes = None,
        runtime_json: bytes = None,
        runtime_data: bytes = None,
        **kwargs: Any
    ) -> Tuple[AttestationResult, AttestationToken]:
        """Attests the validity of an Open Enclave report.

        :param bytes report: An open_enclave report generated from an Intel(tm) SGX enclave
        :keyword bytes inittime_data: Data presented at the time that the SGX
            enclave was initialized.
        :keyword bytes inittime_json: Data presented at the time that the SGX
            enclave was initialized, JSON encoded.
        :keyword bytes runtime_data: Data presented at the time that the open_enclave
            report was created.
        :param bytes runtime_json: Data presented at the time that the open_enclave
            report was created. JSON Encoded.
        :keyword str draft_policy: "draft" or "experimental" policy to be used with
            this attestation request. If this parameter is provided, then this
            policy document will be used for the attestation request.
            This allows a caller to test various policy documents against actual data
            before applying the policy document via the set_policy API.
        :keyword bool validate_token: If True, validate the token, otherwise return the token unvalidated.
        :keyword validation_callback: Function callback to allow clients to perform custom validation of the token.
            if the token is invalid, the `validation_callback` function should throw
            an exception.
        :paramtype validation_callback: ~typing.Callable[[~azure.security.attestation.AttestationToken, ~azure.security.attestation.AttestationSigner], None]
        :keyword bool validate_signature: If True, validate the signature of the token being validated.
        :keyword bool validate_expiration: If True, validate the expiration time of the token being validated.
        :keyword str issuer: Expected issuer, used if `validate_issuer` is true.
        :keyword float validation_slack: Slack time for validation - tolerance applied
            to help account for clock drift between the issuer and the current machine.
        :keyword bool validate_issuer: If True, validate that the issuer of the token matches the expected issuer.
        :keyword bool validate_not_before_time: If true, validate the "Not Before" time in the token.
        :return: :class:`AttestationResult` containing the claims in the returned attestation token.

        :rtype: Tuple[~azure.security.attestation.AttestationResult, ~azure.security.attestation.AttestationToken]

        .. admonition:: Example: Simple OpenEnclave attestation.

            .. literalinclude:: ../samples/sample_attest_enclave_async.py
                :start-after: [START attest_open_enclave_shared]
                :end-before: [END attest_open_enclave_shared]
                :language: python
                :dedent: 8
                :caption: Attesting an open_enclave report for an SGX enclave.

        .. admonition:: Example: Simple OpenEnclave attestation with draft attestation policy.

            .. literalinclude:: ../samples/sample_attest_enclave_async.py
                :start-after: [START attest_open_enclave_shared_draft]
                :end-before: [END attest_open_enclave_shared_draft]
                :language: python
                :dedent: 8
                :caption: Attesting using a draft attestation policy.


        .. note::
            Note that if the `draft_policy` parameter is provided, the resulting
            attestation token will be an unsecured attestation token.

        For additional request configuration options, please see `Python Request
        Options <https://aka.ms/azsdk/python/options>`_.

        """

        if inittime_json and inittime_data:
            raise ValueError("Cannot provide both inittime_json and inittime_data.")
        if runtime_json and runtime_data:
            raise ValueError("Cannot provide both runtime_data and runtime_json.")

        # If the input was JSON, make sure that it's valid JSON before sending it
        # to the service.
        if inittime_json:
            try:
                json.loads(inittime_json)
            except json.JSONDecodeError:
                raise_with_traceback(ValueError, "Content must be valid JSON.")

        if runtime_json:
            try:
                json.loads(runtime_json)
            except json.JSONDecodeError:
                raise_with_traceback(ValueError, "Content must be valid JSON.")

        # Now create the RuntimeData object to be sent to the service.
        runtime = None
        if runtime_data:
            runtime = RuntimeData(data=runtime_data, data_type=DataType.BINARY)

        if runtime_json:
            runtime = RuntimeData(data=runtime_json, data_type=DataType.JSON)

        # And the InitTimeData object to be sent to the service.
        inittime = None
        if inittime_data:
            inittime = InitTimeData(data=inittime_data, data_type=DataType.BINARY)
        if inittime_json:
            inittime = InitTimeData(data=inittime_data, data_type=DataType.JSON)

        request = AttestOpenEnclaveRequest(
            report=report,
            init_time_data=inittime,
            runtime_data=runtime,
            draft_policy_for_attestation=kwargs.pop("draft_policy", None),
        )

        # Merge our existing config options with the options for this API call.
        # Note that this must be done before calling into the implementation
        # layer because the implementation layer doesn't like keyword args that
        # it doesn't expect :(.
        options = merge_validation_args(self._config._kwargs, kwargs)

        result = await self._client.attestation.attest_open_enclave(request, **kwargs)
        token = AttestationToken(
            token=result.token, body_type=GeneratedAttestationResult
        )

        if options.get("validate_token", True):
            token._validate_token(await self._get_signers(**kwargs), **options)
        return (
            AttestationResult._from_generated(token._get_body()),
            token,
        )

    @distributed_trace_async
    async def attest_tpm(self, content: str, **kwargs: Any) -> str:
        """Attest a TPM based enclave.

        See the `TPM Attestation Protocol Reference
        <https://docs.microsoft.com/en-us/azure/attestation/virtualization-based-security-protocol>`_
        for more information.

        :param str content: Data to send to the TPM attestation service.
        :returns: A structure containing the response from the TPM attestation.
        :rtype: str
        """
        response = await self._client.attestation.attest_tpm(
            content.encode("ascii"), **kwargs
        )
        return response.data.decode("ascii")

    async def _get_signers(
        self, **kwargs: Any
    ):  # type: (Any) -> list[AttestationSigner]
        """Returns the set of signing certificates used to sign attestation tokens."""

        with self._statelock:
            if not self._signing_certificates:
                signing_certificates = await self._client.signing_certificates.get(
                    **kwargs
                )
                self._signing_certificates = []
                for key in signing_certificates.keys:
                    self._signing_certificates.append(
                        AttestationSigner._from_generated(key)
                    )
            signers = self._signing_certificates
        return signers

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AttestationClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
