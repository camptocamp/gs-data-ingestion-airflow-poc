from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_event import DatasetEvent


T = TypeVar("T", bound="DatasetEventCollection")


@_attrs_define
class DatasetEventCollection:
    """A collection of dataset events.

    *New in version 2.4.0*

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            dataset_events (Union[Unset, List['DatasetEvent']]):
    """

    total_entries: Union[Unset, int] = UNSET
    dataset_events: Union[Unset, List["DatasetEvent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        dataset_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dataset_events, Unset):
            dataset_events = []
            for dataset_events_item_data in self.dataset_events:
                dataset_events_item = dataset_events_item_data.to_dict()
                dataset_events.append(dataset_events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if dataset_events is not UNSET:
            field_dict["dataset_events"] = dataset_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_event import DatasetEvent

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        dataset_events = []
        _dataset_events = d.pop("dataset_events", UNSET)
        for dataset_events_item_data in _dataset_events or []:
            dataset_events_item = DatasetEvent.from_dict(dataset_events_item_data)

            dataset_events.append(dataset_events_item)

        dataset_event_collection = cls(
            total_entries=total_entries,
            dataset_events=dataset_events,
        )

        dataset_event_collection.additional_properties = d
        return dataset_event_collection

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
