import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventLog")


@_attrs_define
class EventLog:
    """Log of user operations via CLI or Web UI.

    Attributes:
        event_log_id (Union[Unset, int]): The event log ID
        when (Union[Unset, datetime.datetime]): The time when these events happened.
        dag_id (Union[None, Unset, str]): The DAG ID
        task_id (Union[None, Unset, str]): The Task ID
        run_id (Union[None, Unset, str]): The DAG Run ID
        map_index (Union[None, Unset, int]): The Map Index
        try_number (Union[None, Unset, int]): The Try Number
        event (Union[Unset, str]): A key describing the type of event.
        execution_date (Union[None, Unset, datetime.datetime]): When the event was dispatched for an object having
            execution_date, the value of this field.
        owner (Union[None, Unset, str]): Name of the user who triggered these events a.
        extra (Union[None, Unset, str]): Other information that was not included in the other fields, e.g. the complete
            CLI command.
    """

    event_log_id: Union[Unset, int] = UNSET
    when: Union[Unset, datetime.datetime] = UNSET
    dag_id: Union[None, Unset, str] = UNSET
    task_id: Union[None, Unset, str] = UNSET
    run_id: Union[None, Unset, str] = UNSET
    map_index: Union[None, Unset, int] = UNSET
    try_number: Union[None, Unset, int] = UNSET
    event: Union[Unset, str] = UNSET
    execution_date: Union[None, Unset, datetime.datetime] = UNSET
    owner: Union[None, Unset, str] = UNSET
    extra: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_log_id = self.event_log_id

        when: Union[Unset, str] = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        dag_id: Union[None, Unset, str]
        if isinstance(self.dag_id, Unset):
            dag_id = UNSET
        else:
            dag_id = self.dag_id

        task_id: Union[None, Unset, str]
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        run_id: Union[None, Unset, str]
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        map_index: Union[None, Unset, int]
        if isinstance(self.map_index, Unset):
            map_index = UNSET
        else:
            map_index = self.map_index

        try_number: Union[None, Unset, int]
        if isinstance(self.try_number, Unset):
            try_number = UNSET
        else:
            try_number = self.try_number

        event = self.event

        execution_date: Union[None, Unset, str]
        if isinstance(self.execution_date, Unset):
            execution_date = UNSET
        elif isinstance(self.execution_date, datetime.datetime):
            execution_date = self.execution_date.isoformat()
        else:
            execution_date = self.execution_date

        owner: Union[None, Unset, str]
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        extra: Union[None, Unset, str]
        if isinstance(self.extra, Unset):
            extra = UNSET
        else:
            extra = self.extra

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_log_id is not UNSET:
            field_dict["event_log_id"] = event_log_id
        if when is not UNSET:
            field_dict["when"] = when
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if map_index is not UNSET:
            field_dict["map_index"] = map_index
        if try_number is not UNSET:
            field_dict["try_number"] = try_number
        if event is not UNSET:
            field_dict["event"] = event
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if owner is not UNSET:
            field_dict["owner"] = owner
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_log_id = d.pop("event_log_id", UNSET)

        _when = d.pop("when", UNSET)
        when: Union[Unset, datetime.datetime]
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        def _parse_dag_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dag_id = _parse_dag_id(d.pop("dag_id", UNSET))

        def _parse_task_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        def _parse_run_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        run_id = _parse_run_id(d.pop("run_id", UNSET))

        def _parse_map_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        map_index = _parse_map_index(d.pop("map_index", UNSET))

        def _parse_try_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        try_number = _parse_try_number(d.pop("try_number", UNSET))

        event = d.pop("event", UNSET)

        def _parse_execution_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_date_type_0 = isoparse(data)

                return execution_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        execution_date = _parse_execution_date(d.pop("execution_date", UNSET))

        def _parse_owner(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_extra(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extra = _parse_extra(d.pop("extra", UNSET))

        event_log = cls(
            event_log_id=event_log_id,
            when=when,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            event=event,
            execution_date=execution_date,
            owner=owner,
            extra=extra,
        )

        event_log.additional_properties = d
        return event_log

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
