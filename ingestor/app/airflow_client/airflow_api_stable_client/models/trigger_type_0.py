from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerType0")


@_attrs_define
class TriggerType0:
    """
    Attributes:
        id (Union[Unset, int]):
        classpath (Union[Unset, str]):
        kwargs (Union[Unset, str]):
        created_date (Union[Unset, str]):
        triggerer_id (Union[None, Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    classpath: Union[Unset, str] = UNSET
    kwargs: Union[Unset, str] = UNSET
    created_date: Union[Unset, str] = UNSET
    triggerer_id: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        classpath = self.classpath

        kwargs = self.kwargs

        created_date = self.created_date

        triggerer_id: Union[None, Unset, int]
        if isinstance(self.triggerer_id, Unset):
            triggerer_id = UNSET
        else:
            triggerer_id = self.triggerer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if classpath is not UNSET:
            field_dict["classpath"] = classpath
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if triggerer_id is not UNSET:
            field_dict["triggerer_id"] = triggerer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        classpath = d.pop("classpath", UNSET)

        kwargs = d.pop("kwargs", UNSET)

        created_date = d.pop("created_date", UNSET)

        def _parse_triggerer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        triggerer_id = _parse_triggerer_id(d.pop("triggerer_id", UNSET))

        trigger_type_0 = cls(
            id=id,
            classpath=classpath,
            kwargs=kwargs,
            created_date=created_date,
            triggerer_id=triggerer_id,
        )

        trigger_type_0.additional_properties = d
        return trigger_type_0

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
