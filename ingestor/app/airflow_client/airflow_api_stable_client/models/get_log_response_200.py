from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLogResponse200")


@_attrs_define
class GetLogResponse200:
    """
    Attributes:
        continuation_token (Union[Unset, str]):
        content (Union[Unset, str]):
    """

    continuation_token: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        continuation_token = self.continuation_token

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        continuation_token = d.pop("continuation_token", UNSET)

        content = d.pop("content", UNSET)

        get_log_response_200 = cls(
            continuation_token=continuation_token,
            content=content,
        )

        get_log_response_200.additional_properties = d
        return get_log_response_200

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
