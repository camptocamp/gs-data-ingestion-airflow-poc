from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_stats_state_collection_item import DagStatsStateCollectionItem


T = TypeVar("T", bound="DagStatsCollectionItem")


@_attrs_define
class DagStatsCollectionItem:
    """DagStats entry collection item.

    Attributes:
        dag_id (Union[Unset, str]): The DAG ID.
        stats (Union[List['DagStatsStateCollectionItem'], None, Unset]):
    """

    dag_id: Union[Unset, str] = UNSET
    stats: Union[List["DagStatsStateCollectionItem"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dag_id = self.dag_id

        stats: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, list):
            stats = []
            for stats_type_0_item_data in self.stats:
                stats_type_0_item = stats_type_0_item_data.to_dict()
                stats.append(stats_type_0_item)

        else:
            stats = self.stats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dag_stats_state_collection_item import DagStatsStateCollectionItem

        d = src_dict.copy()
        dag_id = d.pop("dag_id", UNSET)

        def _parse_stats(data: object) -> Union[List["DagStatsStateCollectionItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stats_type_0 = []
                _stats_type_0 = data
                for stats_type_0_item_data in _stats_type_0:
                    stats_type_0_item = DagStatsStateCollectionItem.from_dict(stats_type_0_item_data)

                    stats_type_0.append(stats_type_0_item)

                return stats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["DagStatsStateCollectionItem"], None, Unset], data)

        stats = _parse_stats(d.pop("stats", UNSET))

        dag_stats_collection_item = cls(
            dag_id=dag_id,
            stats=stats,
        )

        dag_stats_collection_item.additional_properties = d
        return dag_stats_collection_item

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
