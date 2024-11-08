import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_state_type_1 import TaskStateType1
from ..models.task_state_type_2_type_1 import TaskStateType2Type1
from ..models.task_state_type_3_type_1 import TaskStateType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTaskInstanceForm")


@_attrs_define
class ListTaskInstanceForm:
    """
    Attributes:
        page_offset (Union[Unset, int]): The number of items to skip before starting to collect the result set.
        page_limit (Union[Unset, int]): The numbers of items to return. Default: 100.
        dag_ids (Union[Unset, List[str]]): Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).
        dag_run_ids (Union[Unset, List[str]]): Return objects with specific DAG Run IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).
            *New in version 2.7.1*
        task_ids (Union[Unset, List[str]]): Return objects with specific task IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).
            *New in version 2.7.1*
        execution_date_gte (Union[Unset, datetime.datetime]): Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.
        execution_date_lte (Union[Unset, datetime.datetime]): Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.
        start_date_gte (Union[Unset, datetime.datetime]): Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.
        start_date_lte (Union[Unset, datetime.datetime]): Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.
        end_date_gte (Union[Unset, datetime.datetime]): Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.
        end_date_lte (Union[Unset, datetime.datetime]): Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.
        duration_gte (Union[Unset, float]): Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.
        duration_lte (Union[Unset, float]): Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.
        state (Union[Unset, List[Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1]]]): The value can
            be repeated to retrieve multiple matching values (OR condition).
        pool (Union[Unset, List[str]]): The value can be repeated to retrieve multiple matching values (OR condition).
        queue (Union[Unset, List[str]]): The value can be repeated to retrieve multiple matching values (OR condition).
        executor (Union[Unset, List[str]]): The value can be repeated to retrieve multiple matching values (OR
            condition).
    """

    page_offset: Union[Unset, int] = UNSET
    page_limit: Union[Unset, int] = 100
    dag_ids: Union[Unset, List[str]] = UNSET
    dag_run_ids: Union[Unset, List[str]] = UNSET
    task_ids: Union[Unset, List[str]] = UNSET
    execution_date_gte: Union[Unset, datetime.datetime] = UNSET
    execution_date_lte: Union[Unset, datetime.datetime] = UNSET
    start_date_gte: Union[Unset, datetime.datetime] = UNSET
    start_date_lte: Union[Unset, datetime.datetime] = UNSET
    end_date_gte: Union[Unset, datetime.datetime] = UNSET
    end_date_lte: Union[Unset, datetime.datetime] = UNSET
    duration_gte: Union[Unset, float] = UNSET
    duration_lte: Union[Unset, float] = UNSET
    state: Union[Unset, List[Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1]]] = UNSET
    pool: Union[Unset, List[str]] = UNSET
    queue: Union[Unset, List[str]] = UNSET
    executor: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_offset = self.page_offset

        page_limit = self.page_limit

        dag_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dag_ids, Unset):
            dag_ids = self.dag_ids

        dag_run_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dag_run_ids, Unset):
            dag_run_ids = self.dag_run_ids

        task_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.task_ids, Unset):
            task_ids = self.task_ids

        execution_date_gte: Union[Unset, str] = UNSET
        if not isinstance(self.execution_date_gte, Unset):
            execution_date_gte = self.execution_date_gte.isoformat()

        execution_date_lte: Union[Unset, str] = UNSET
        if not isinstance(self.execution_date_lte, Unset):
            execution_date_lte = self.execution_date_lte.isoformat()

        start_date_gte: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_gte, Unset):
            start_date_gte = self.start_date_gte.isoformat()

        start_date_lte: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_lte, Unset):
            start_date_lte = self.start_date_lte.isoformat()

        end_date_gte: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_gte, Unset):
            end_date_gte = self.end_date_gte.isoformat()

        end_date_lte: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_lte, Unset):
            end_date_lte = self.end_date_lte.isoformat()

        duration_gte = self.duration_gte

        duration_lte = self.duration_lte

        state: Union[Unset, List[Union[None, str]]] = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item: Union[None, str]
                if isinstance(state_item_data, TaskStateType1):
                    state_item = state_item_data.value
                elif isinstance(state_item_data, TaskStateType2Type1):
                    state_item = state_item_data.value
                elif isinstance(state_item_data, TaskStateType3Type1):
                    state_item = state_item_data.value
                else:
                    state_item = state_item_data
                state.append(state_item)

        pool: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool

        queue: Union[Unset, List[str]] = UNSET
        if not isinstance(self.queue, Unset):
            queue = self.queue

        executor: Union[Unset, List[str]] = UNSET
        if not isinstance(self.executor, Unset):
            executor = self.executor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_offset is not UNSET:
            field_dict["page_offset"] = page_offset
        if page_limit is not UNSET:
            field_dict["page_limit"] = page_limit
        if dag_ids is not UNSET:
            field_dict["dag_ids"] = dag_ids
        if dag_run_ids is not UNSET:
            field_dict["dag_run_ids"] = dag_run_ids
        if task_ids is not UNSET:
            field_dict["task_ids"] = task_ids
        if execution_date_gte is not UNSET:
            field_dict["execution_date_gte"] = execution_date_gte
        if execution_date_lte is not UNSET:
            field_dict["execution_date_lte"] = execution_date_lte
        if start_date_gte is not UNSET:
            field_dict["start_date_gte"] = start_date_gte
        if start_date_lte is not UNSET:
            field_dict["start_date_lte"] = start_date_lte
        if end_date_gte is not UNSET:
            field_dict["end_date_gte"] = end_date_gte
        if end_date_lte is not UNSET:
            field_dict["end_date_lte"] = end_date_lte
        if duration_gte is not UNSET:
            field_dict["duration_gte"] = duration_gte
        if duration_lte is not UNSET:
            field_dict["duration_lte"] = duration_lte
        if state is not UNSET:
            field_dict["state"] = state
        if pool is not UNSET:
            field_dict["pool"] = pool
        if queue is not UNSET:
            field_dict["queue"] = queue
        if executor is not UNSET:
            field_dict["executor"] = executor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_offset = d.pop("page_offset", UNSET)

        page_limit = d.pop("page_limit", UNSET)

        dag_ids = cast(List[str], d.pop("dag_ids", UNSET))

        dag_run_ids = cast(List[str], d.pop("dag_run_ids", UNSET))

        task_ids = cast(List[str], d.pop("task_ids", UNSET))

        _execution_date_gte = d.pop("execution_date_gte", UNSET)
        execution_date_gte: Union[Unset, datetime.datetime]
        if isinstance(_execution_date_gte, Unset):
            execution_date_gte = UNSET
        else:
            execution_date_gte = isoparse(_execution_date_gte)

        _execution_date_lte = d.pop("execution_date_lte", UNSET)
        execution_date_lte: Union[Unset, datetime.datetime]
        if isinstance(_execution_date_lte, Unset):
            execution_date_lte = UNSET
        else:
            execution_date_lte = isoparse(_execution_date_lte)

        _start_date_gte = d.pop("start_date_gte", UNSET)
        start_date_gte: Union[Unset, datetime.datetime]
        if isinstance(_start_date_gte, Unset):
            start_date_gte = UNSET
        else:
            start_date_gte = isoparse(_start_date_gte)

        _start_date_lte = d.pop("start_date_lte", UNSET)
        start_date_lte: Union[Unset, datetime.datetime]
        if isinstance(_start_date_lte, Unset):
            start_date_lte = UNSET
        else:
            start_date_lte = isoparse(_start_date_lte)

        _end_date_gte = d.pop("end_date_gte", UNSET)
        end_date_gte: Union[Unset, datetime.datetime]
        if isinstance(_end_date_gte, Unset):
            end_date_gte = UNSET
        else:
            end_date_gte = isoparse(_end_date_gte)

        _end_date_lte = d.pop("end_date_lte", UNSET)
        end_date_lte: Union[Unset, datetime.datetime]
        if isinstance(_end_date_lte, Unset):
            end_date_lte = UNSET
        else:
            end_date_lte = isoparse(_end_date_lte)

        duration_gte = d.pop("duration_gte", UNSET)

        duration_lte = d.pop("duration_lte", UNSET)

        state = []
        _state = d.pop("state", UNSET)
        for state_item_data in _state or []:

            def _parse_state_item(
                data: object,
            ) -> Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    componentsschemas_task_state_type_1 = TaskStateType1(data)

                    return componentsschemas_task_state_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    componentsschemas_task_state_type_2_type_1 = TaskStateType2Type1(data)

                    return componentsschemas_task_state_type_2_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    componentsschemas_task_state_type_3_type_1 = TaskStateType3Type1(data)

                    return componentsschemas_task_state_type_3_type_1
                except:  # noqa: E722
                    pass
                return cast(Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1], data)

            state_item = _parse_state_item(state_item_data)

            state.append(state_item)

        pool = cast(List[str], d.pop("pool", UNSET))

        queue = cast(List[str], d.pop("queue", UNSET))

        executor = cast(List[str], d.pop("executor", UNSET))

        list_task_instance_form = cls(
            page_offset=page_offset,
            page_limit=page_limit,
            dag_ids=dag_ids,
            dag_run_ids=dag_run_ids,
            task_ids=task_ids,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            state=state,
            pool=pool,
            queue=queue,
            executor=executor,
        )

        list_task_instance_form.additional_properties = d
        return list_task_instance_form

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
