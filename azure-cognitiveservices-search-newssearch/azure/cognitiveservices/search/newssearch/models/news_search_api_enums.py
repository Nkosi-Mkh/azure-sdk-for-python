# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ErrorCode(Enum):

    none = "None"
    server_error = "ServerError"
    invalid_request = "InvalidRequest"
    rate_limit_exceeded = "RateLimitExceeded"
    invalid_authorization = "InvalidAuthorization"
    insufficient_authorization = "InsufficientAuthorization"


class ErrorSubCode(Enum):

    unexpected_error = "UnexpectedError"
    resource_error = "ResourceError"
    not_implemented = "NotImplemented"
    parameter_missing = "ParameterMissing"
    parameter_invalid_value = "ParameterInvalidValue"
    http_not_allowed = "HttpNotAllowed"
    blocked = "Blocked"
    authorization_missing = "AuthorizationMissing"
    authorization_redundancy = "AuthorizationRedundancy"
    authorization_disabled = "AuthorizationDisabled"
    authorization_expired = "AuthorizationExpired"


class Freshness(Enum):

    day = "Day"
    week = "Week"
    month = "Month"


class SafeSearch(Enum):

    off = "Off"
    moderate = "Moderate"
    strict = "Strict"


class TextFormat(Enum):

    raw = "Raw"
    html = "Html"
