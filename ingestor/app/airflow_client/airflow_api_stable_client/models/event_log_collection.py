from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_log import EventLog


T = TypeVar("T", bound="EventLogCollection")


@_attrs_define
class EventLogCollection:
    """Collection of event logs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    *Changed in version 2.10.0*&#58; 'try_number' and 'map_index' fields are added.

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            event_logs (Union[Unset, List['EventLog']]):
    """

    total_entries: Union[Unset, int] = UNSET
    event_logs: Union[Unset, List["EventLog"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        event_logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.event_logs, Unset):
            event_logs = []
            for event_logs_item_data in self.event_logs:
                event_logs_item = event_logs_item_data.to_dict()
                event_logs.append(event_logs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if event_logs is not UNSET:
            field_dict["event_logs"] = event_logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_log import EventLog

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        event_logs = []
        _event_logs = d.pop("event_logs", UNSET)
        for event_logs_item_data in _event_logs or []:
            event_logs_item = EventLog.from_dict(event_logs_item_data)

            event_logs.append(event_logs_item)

        event_log_collection = cls(
            total_entries=total_entries,
            event_logs=event_logs,
        )

        event_log_collection.additional_properties = d
        return event_log_collection

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
