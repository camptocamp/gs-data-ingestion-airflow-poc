from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Connection")


@_attrs_define
class Connection:
    """Full representation of the connection.

    Attributes:
        connection_id (Union[Unset, str]): The connection ID.
        conn_type (Union[Unset, str]): The connection type.
        description (Union[None, Unset, str]): The description of the connection.
        host (Union[None, Unset, str]): Host of the connection.
        login (Union[None, Unset, str]): Login of the connection.
        schema (Union[None, Unset, str]): Schema of the connection.
        port (Union[None, Unset, int]): Port of the connection.
        password (Union[Unset, str]): Password of the connection.
        extra (Union[None, Unset, str]): Other values that cannot be put into another field, e.g. RSA keys.
    """

    connection_id: Union[Unset, str] = UNSET
    conn_type: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    host: Union[None, Unset, str] = UNSET
    login: Union[None, Unset, str] = UNSET
    schema: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, int] = UNSET
    password: Union[Unset, str] = UNSET
    extra: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        conn_type = self.conn_type

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        login: Union[None, Unset, str]
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        schema: Union[None, Unset, str]
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        password = self.password

        extra: Union[None, Unset, str]
        if isinstance(self.extra, Unset):
            extra = UNSET
        else:
            extra = self.extra

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if conn_type is not UNSET:
            field_dict["conn_type"] = conn_type
        if description is not UNSET:
            field_dict["description"] = description
        if host is not UNSET:
            field_dict["host"] = host
        if login is not UNSET:
            field_dict["login"] = login
        if schema is not UNSET:
            field_dict["schema"] = schema
        if port is not UNSET:
            field_dict["port"] = port
        if password is not UNSET:
            field_dict["password"] = password
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id", UNSET)

        conn_type = d.pop("conn_type", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_login(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        login = _parse_login(d.pop("login", UNSET))

        def _parse_schema(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        password = d.pop("password", UNSET)

        def _parse_extra(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extra = _parse_extra(d.pop("extra", UNSET))

        connection = cls(
            connection_id=connection_id,
            conn_type=conn_type,
            description=description,
            host=host,
            login=login,
            schema=schema,
            port=port,
            password=password,
            extra=extra,
        )

        connection.additional_properties = d
        return connection

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
