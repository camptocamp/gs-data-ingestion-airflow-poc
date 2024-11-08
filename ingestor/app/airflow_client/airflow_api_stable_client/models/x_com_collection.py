from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x_com_collection_item import XComCollectionItem


T = TypeVar("T", bound="XComCollection")


@_attrs_define
class XComCollection:
    """Collection of XCom entries.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            xcom_entries (Union[Unset, List['XComCollectionItem']]):
    """

    total_entries: Union[Unset, int] = UNSET
    xcom_entries: Union[Unset, List["XComCollectionItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        xcom_entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.xcom_entries, Unset):
            xcom_entries = []
            for xcom_entries_item_data in self.xcom_entries:
                xcom_entries_item = xcom_entries_item_data.to_dict()
                xcom_entries.append(xcom_entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if xcom_entries is not UNSET:
            field_dict["xcom_entries"] = xcom_entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.x_com_collection_item import XComCollectionItem

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        xcom_entries = []
        _xcom_entries = d.pop("xcom_entries", UNSET)
        for xcom_entries_item_data in _xcom_entries or []:
            xcom_entries_item = XComCollectionItem.from_dict(xcom_entries_item_data)

            xcom_entries.append(xcom_entries_item)

        x_com_collection = cls(
            total_entries=total_entries,
            xcom_entries=xcom_entries,
        )

        x_com_collection.additional_properties = d
        return x_com_collection

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
