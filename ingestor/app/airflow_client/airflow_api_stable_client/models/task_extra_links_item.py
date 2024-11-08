from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.class_reference import ClassReference


T = TypeVar("T", bound="TaskExtraLinksItem")


@_attrs_define
class TaskExtraLinksItem:
    """
    Attributes:
        class_ref (Union[Unset, ClassReference]): Class reference
    """

    class_ref: Union[Unset, "ClassReference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        class_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.class_ref, Unset):
            class_ref = self.class_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_ref is not UNSET:
            field_dict["class_ref"] = class_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.class_reference import ClassReference

        d = src_dict.copy()
        _class_ref = d.pop("class_ref", UNSET)
        class_ref: Union[Unset, ClassReference]
        if isinstance(_class_ref, Unset):
            class_ref = UNSET
        else:
            class_ref = ClassReference.from_dict(_class_ref)

        task_extra_links_item = cls(
            class_ref=class_ref,
        )

        task_extra_links_item.additional_properties = d
        return task_extra_links_item

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
