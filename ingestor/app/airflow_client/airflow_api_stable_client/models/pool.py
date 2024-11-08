from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pool")


@_attrs_define
class Pool:
    """The pool

    Attributes:
        name (Union[Unset, str]): The name of pool.
        slots (Union[Unset, int]): The maximum number of slots that can be assigned to tasks. One job may occupy one or
            more slots.
        occupied_slots (Union[Unset, int]): The number of slots used by running/queued tasks at the moment. May include
            deferred tasks if 'include_deferred' is set to true.
        running_slots (Union[Unset, int]): The number of slots used by running tasks at the moment.
        queued_slots (Union[Unset, int]): The number of slots used by queued tasks at the moment.
        open_slots (Union[Unset, int]): The number of free slots at the moment.
        scheduled_slots (Union[Unset, int]): The number of slots used by scheduled tasks at the moment.
        deferred_slots (Union[Unset, int]): The number of slots used by deferred tasks at the moment. Relevant if
            'include_deferred' is set to true.

            *New in version 2.7.0*
        description (Union[None, Unset, str]): The description of the pool.

            *New in version 2.3.0*
        include_deferred (Union[Unset, bool]): If set to true, deferred tasks are considered when calculating open pool
            slots.

            *New in version 2.7.0*
    """

    name: Union[Unset, str] = UNSET
    slots: Union[Unset, int] = UNSET
    occupied_slots: Union[Unset, int] = UNSET
    running_slots: Union[Unset, int] = UNSET
    queued_slots: Union[Unset, int] = UNSET
    open_slots: Union[Unset, int] = UNSET
    scheduled_slots: Union[Unset, int] = UNSET
    deferred_slots: Union[Unset, int] = UNSET
    description: Union[None, Unset, str] = UNSET
    include_deferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        slots = self.slots

        occupied_slots = self.occupied_slots

        running_slots = self.running_slots

        queued_slots = self.queued_slots

        open_slots = self.open_slots

        scheduled_slots = self.scheduled_slots

        deferred_slots = self.deferred_slots

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        include_deferred = self.include_deferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slots is not UNSET:
            field_dict["slots"] = slots
        if occupied_slots is not UNSET:
            field_dict["occupied_slots"] = occupied_slots
        if running_slots is not UNSET:
            field_dict["running_slots"] = running_slots
        if queued_slots is not UNSET:
            field_dict["queued_slots"] = queued_slots
        if open_slots is not UNSET:
            field_dict["open_slots"] = open_slots
        if scheduled_slots is not UNSET:
            field_dict["scheduled_slots"] = scheduled_slots
        if deferred_slots is not UNSET:
            field_dict["deferred_slots"] = deferred_slots
        if description is not UNSET:
            field_dict["description"] = description
        if include_deferred is not UNSET:
            field_dict["include_deferred"] = include_deferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        slots = d.pop("slots", UNSET)

        occupied_slots = d.pop("occupied_slots", UNSET)

        running_slots = d.pop("running_slots", UNSET)

        queued_slots = d.pop("queued_slots", UNSET)

        open_slots = d.pop("open_slots", UNSET)

        scheduled_slots = d.pop("scheduled_slots", UNSET)

        deferred_slots = d.pop("deferred_slots", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        include_deferred = d.pop("include_deferred", UNSET)

        pool = cls(
            name=name,
            slots=slots,
            occupied_slots=occupied_slots,
            running_slots=running_slots,
            queued_slots=queued_slots,
            open_slots=open_slots,
            scheduled_slots=scheduled_slots,
            deferred_slots=deferred_slots,
            description=description,
            include_deferred=include_deferred,
        )

        pool.additional_properties = d
        return pool

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
