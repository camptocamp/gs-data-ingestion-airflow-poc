from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool import Pool


T = TypeVar("T", bound="PoolCollection")


@_attrs_define
class PoolCollection:
    """Collection of pools.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            pools (Union[Unset, List['Pool']]):
    """

    total_entries: Union[Unset, int] = UNSET
    pools: Union[Unset, List["Pool"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        pools: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pools, Unset):
            pools = []
            for pools_item_data in self.pools:
                pools_item = pools_item_data.to_dict()
                pools.append(pools_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if pools is not UNSET:
            field_dict["pools"] = pools

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pool import Pool

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        pools = []
        _pools = d.pop("pools", UNSET)
        for pools_item_data in _pools or []:
            pools_item = Pool.from_dict(pools_item_data)

            pools.append(pools_item)

        pool_collection = cls(
            total_entries=total_entries,
            pools=pools,
        )

        pool_collection.additional_properties = d
        return pool_collection

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
