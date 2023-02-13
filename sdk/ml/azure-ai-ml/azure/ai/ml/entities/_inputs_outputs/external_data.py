# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Optional, List, Dict, Union

from inspect import Parameter

from azure.ai.ml.entities._mixins import DictMixin, RestTranslatableMixin
from azure.ai.ml.entities._inputs_outputs.utils import _remove_empty_values
from azure.ai.ml.constants._component import ExternalDataType


class StoredProcedureParameter(DictMixin, RestTranslatableMixin):
    """Define a stored procedure parameter class for DataTransfer import database task.


    :param type: The type of the database stored procedure
    :type type: str
    :param name: The name of the database stored procedure
    :type name: str
    :param value: The value of the database stored procedure
    :type value: str
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        type: Optional[str] = None, # pylint: disable=redefined-builtin
    ):
        self.type = type
        self.name = name
        self.value = value


class Database(DictMixin, RestTranslatableMixin):  # pylint: disable=too-many-instance-attributes
    """Define a database class for a DataTransfer Component or Job.

    e.g.
    source_snowflake = Database(query='SELECT * FROM my_table', connection='azureml:my_azuresql_connection')
    or
    stored_procedure_params = [{'name': 'job', 'value': 'Engineer', 'type': 'String'},
    {'name': 'department', 'value': 'Engineering', 'type': 'String'}]
    source_snowflake = Database(stored_procedure='SelectEmployeeByJobAndDepartment',
                                stored_procedure_params=stored_procedure_params,
                                connection='azureml:my_azuresql_connection')

    :param type: The type of the data input. Possible values include: 'file_system', 'database'.
    :type type: str
    :param query: The sql query to get data from database
    :type query: str
    :param table_name: The database table name
    :type table_name: str
    :param stored_procedure: stored_procedure
    :type stored_procedure: str
    :param stored_procedure_params: stored_procedure_params
    :type stored_procedure_params: List[dict, StoredProcedureParameter]
    :param connection: Connection is workspace, we didn't support storage connection here, need leverage workspace
    connection to store these credential info.
    :type connection: str
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if Source cannot be successfully validated.
        Details will be provided in the error message.
    """

    _EMPTY = Parameter.empty

    def __init__(
        self,
        *,
        type: Optional[str] = ExternalDataType.DATABASE,  # pylint: disable=redefined-builtin
        query: Optional[str] = None,
        table_name: Optional[str] = None,
        stored_procedure: Optional[str] = None,
        stored_procedure_params: Optional[List[dict]] = None,
        connection: Optional[str] = None,
    ):
        # As an annotation, it is not allowed to initialize the name.
        # The name will be updated by the annotated variable name.
        self.type = type
        self.name = None
        self.connection = connection
        self.query = query
        self.table_name = table_name
        self.stored_procedure = stored_procedure
        self.stored_procedure_params = stored_procedure_params

    def _to_dict(self, remove_name=True):
        """Convert the Source object to a dict."""
        keys = ["name", "type", "query", "stored_procedure", "stored_procedure_params", "connection", "table_name"]
        if remove_name:
            keys.remove("name")
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    def _to_rest_object(self) -> Dict:
        # this is for component rest object when using Source as component inputs, as for job input usage,
        # rest object is generated by extracting Source's properties, see details in to_rest_dataset_literal_inputs()
        result = self._to_dict()
        return result

    def _update_name(self, name):
        self.name = name

    @classmethod
    def _from_rest_object(cls, obj: Dict) -> "Database":
        return Database(**obj)

    @property
    def stored_procedure_params(self) -> Optional[StoredProcedureParameter]:
        """Compute Resource configuration for the job."""

        return self._stored_procedure_params

    @stored_procedure_params.setter
    def stored_procedure_params(self, value: Union[Dict[str, str], StoredProcedureParameter, None]):
        if value is None:
            self._stored_procedure_params = value
        else:
            if not isinstance(value, list):
                value = [value]
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    value[index] = StoredProcedureParameter(**item)
            self._stored_procedure_params = value


class FileSystem(DictMixin, RestTranslatableMixin):  # pylint: disable=too-many-instance-attributes
    """Define a file system class of a DataTransfer Component or Job.

    e.g. source_s3 = FileSystem(path='s3://my_bucket/my_folder', connection='azureml:my_s3_connection')

    The init function of Group will be 'def __init__(self, *, int_param0, int_param3, int_param1=1)'.
    :param type: The type of the data input. Possible values include: 'file_system', 'database'.
    :type type: str
    :param path: The path to which the input is pointing. Could be pointing to the path of file system.
    :type path: str
    :param connection: Connection is workspace, we didn't support storage connection here, need leverage workspace
    connection to store these credential info.
    :type connection: str
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if Source cannot be successfully validated.
        Details will be provided in the error message.
    """
    _EMPTY = Parameter.empty

    def __init__(
        self,
        *,
        type: Optional[str] = ExternalDataType.FILE_SYSTEM,  # pylint: disable=redefined-builtin
        path: Optional[str] = None,
        connection: Optional[str] = None,
    ):
        self.type = type
        self.name = None
        self.connection = connection

        if path is not None and not isinstance(path, str):
            # this logic will make dsl data binding expression working in the same way as yaml
            # it's written to handle InputOutputBase, but there will be loop import if we import InputOutputBase here
            self.path = str(path)
        else:
            self.path = path

    def _to_dict(self, remove_name=True):
        """Convert the Source object to a dict."""
        keys = ["name", "path", "type", "connection"]
        if remove_name:
            keys.remove("name")
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    def _to_rest_object(self) -> Dict:
        # this is for component rest object when using Source as component inputs, as for job input usage,
        # rest object is generated by extracting Source's properties, see details in to_rest_dataset_literal_inputs()
        result = self._to_dict()
        return result

    def _update_name(self, name):
        self.name = name

    @classmethod
    def _from_rest_object(cls, obj: Dict) -> "FileSystem":
        return FileSystem(**obj)