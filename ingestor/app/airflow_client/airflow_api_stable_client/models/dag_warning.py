from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DagWarning")


@_attrs_define
class DagWarning:
    """
    Attributes:
        dag_id (Union[Unset, str]): The dag_id.
        warning_type (Union[Unset, str]): The warning type for the dag warning.
        message (Union[Unset, str]): The message for the dag warning.
        timestamp (Union[Unset, str]): The time when this warning was logged.
    """

    dag_id: Union[Unset, str] = UNSET
    warning_type: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dag_id = self.dag_id

        warning_type = self.warning_type

        message = self.message

        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if warning_type is not UNSET:
            field_dict["warning_type"] = warning_type
        if message is not UNSET:
            field_dict["message"] = message
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dag_id = d.pop("dag_id", UNSET)

        warning_type = d.pop("warning_type", UNSET)

        message = d.pop("message", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        dag_warning = cls(
            dag_id=dag_id,
            warning_type=warning_type,
            message=message,
            timestamp=timestamp,
        )

        dag_warning.additional_properties = d
        return dag_warning

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
