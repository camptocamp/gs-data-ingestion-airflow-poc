from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_state_type_1 import TaskStateType1
from ..models.task_state_type_2_type_1 import TaskStateType2Type1
from ..models.task_state_type_3_type_1 import TaskStateType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_type_0 import JobType0
    from ..models.sla_miss_type_0 import SLAMissType0
    from ..models.task_instance_rendered_fields import TaskInstanceRenderedFields
    from ..models.trigger_type_0 import TriggerType0


T = TypeVar("T", bound="TaskInstance")


@_attrs_define
class TaskInstance:
    """
    Attributes:
        task_id (Union[Unset, str]):
        task_display_name (Union[Unset, str]): Human centric display text for the task.

            *New in version 2.9.0*
        dag_id (Union[Unset, str]):
        dag_run_id (Union[Unset, str]): The DagRun ID for this task instance

            *New in version 2.3.0*
        execution_date (Union[Unset, str]):
        start_date (Union[None, Unset, str]):
        end_date (Union[None, Unset, str]):
        duration (Union[None, Unset, float]):
        state (Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1, Unset]): Task state.

            *Changed in version 2.0.2*&#58; 'removed' is added as a possible value.

            *Changed in version 2.2.0*&#58; 'deferred' is added as a possible value.

            *Changed in version 2.4.0*&#58; 'sensing' state has been removed.
            *Changed in version 2.4.2*&#58; 'restarting' is added as a possible value

            *Changed in version 2.7.0*&#58; Field becomes nullable and null primitive is added as a possible value.
            *Changed in version 2.7.0*&#58; 'none' state is deprecated in favor of null.
        try_number (Union[Unset, int]):
        map_index (Union[Unset, int]):
        max_tries (Union[Unset, int]):
        hostname (Union[Unset, str]):
        unixname (Union[Unset, str]):
        pool (Union[Unset, str]):
        pool_slots (Union[Unset, int]):
        queue (Union[None, Unset, str]):
        priority_weight (Union[None, Unset, int]):
        operator (Union[None, Unset, str]): *Changed in version 2.1.1*&#58; Field becomes nullable.
        queued_when (Union[None, Unset, str]): The datetime that the task enter the state QUEUE, also known as queue_at
        pid (Union[None, Unset, int]):
        executor (Union[None, Unset, str]): Executor the task is configured to run on or None (which indicates the
            default executor)

            *New in version 2.10.0*
        executor_config (Union[Unset, str]):
        sla_miss (Union['SLAMissType0', None, Unset]):
        rendered_map_index (Union[None, Unset, str]): Rendered name of an expanded task instance, if the task is mapped.

            *New in version 2.9.0*
        rendered_fields (Union[Unset, TaskInstanceRenderedFields]): JSON object describing rendered fields.

            *New in version 2.3.0*
        trigger (Union['TriggerType0', None, Unset]):
        triggerer_job (Union['JobType0', None, Unset]):
        note (Union[None, Unset, str]): Contains manually entered notes by the user about the TaskInstance.

            *New in version 2.5.0*
    """

    task_id: Union[Unset, str] = UNSET
    task_display_name: Union[Unset, str] = UNSET
    dag_id: Union[Unset, str] = UNSET
    dag_run_id: Union[Unset, str] = UNSET
    execution_date: Union[Unset, str] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    duration: Union[None, Unset, float] = UNSET
    state: Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1, Unset] = UNSET
    try_number: Union[Unset, int] = UNSET
    map_index: Union[Unset, int] = UNSET
    max_tries: Union[Unset, int] = UNSET
    hostname: Union[Unset, str] = UNSET
    unixname: Union[Unset, str] = UNSET
    pool: Union[Unset, str] = UNSET
    pool_slots: Union[Unset, int] = UNSET
    queue: Union[None, Unset, str] = UNSET
    priority_weight: Union[None, Unset, int] = UNSET
    operator: Union[None, Unset, str] = UNSET
    queued_when: Union[None, Unset, str] = UNSET
    pid: Union[None, Unset, int] = UNSET
    executor: Union[None, Unset, str] = UNSET
    executor_config: Union[Unset, str] = UNSET
    sla_miss: Union["SLAMissType0", None, Unset] = UNSET
    rendered_map_index: Union[None, Unset, str] = UNSET
    rendered_fields: Union[Unset, "TaskInstanceRenderedFields"] = UNSET
    trigger: Union["TriggerType0", None, Unset] = UNSET
    triggerer_job: Union["JobType0", None, Unset] = UNSET
    note: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.job_type_0 import JobType0
        from ..models.sla_miss_type_0 import SLAMissType0
        from ..models.trigger_type_0 import TriggerType0

        task_id = self.task_id

        task_display_name = self.task_display_name

        dag_id = self.dag_id

        dag_run_id = self.dag_run_id

        execution_date = self.execution_date

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        duration: Union[None, Unset, float]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, TaskStateType1):
            state = self.state.value
        elif isinstance(self.state, TaskStateType2Type1):
            state = self.state.value
        elif isinstance(self.state, TaskStateType3Type1):
            state = self.state.value
        else:
            state = self.state

        try_number = self.try_number

        map_index = self.map_index

        max_tries = self.max_tries

        hostname = self.hostname

        unixname = self.unixname

        pool = self.pool

        pool_slots = self.pool_slots

        queue: Union[None, Unset, str]
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        priority_weight: Union[None, Unset, int]
        if isinstance(self.priority_weight, Unset):
            priority_weight = UNSET
        else:
            priority_weight = self.priority_weight

        operator: Union[None, Unset, str]
        if isinstance(self.operator, Unset):
            operator = UNSET
        else:
            operator = self.operator

        queued_when: Union[None, Unset, str]
        if isinstance(self.queued_when, Unset):
            queued_when = UNSET
        else:
            queued_when = self.queued_when

        pid: Union[None, Unset, int]
        if isinstance(self.pid, Unset):
            pid = UNSET
        else:
            pid = self.pid

        executor: Union[None, Unset, str]
        if isinstance(self.executor, Unset):
            executor = UNSET
        else:
            executor = self.executor

        executor_config = self.executor_config

        sla_miss: Union[Dict[str, Any], None, Unset]
        if isinstance(self.sla_miss, Unset):
            sla_miss = UNSET
        elif isinstance(self.sla_miss, SLAMissType0):
            sla_miss = self.sla_miss.to_dict()
        else:
            sla_miss = self.sla_miss

        rendered_map_index: Union[None, Unset, str]
        if isinstance(self.rendered_map_index, Unset):
            rendered_map_index = UNSET
        else:
            rendered_map_index = self.rendered_map_index

        rendered_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rendered_fields, Unset):
            rendered_fields = self.rendered_fields.to_dict()

        trigger: Union[Dict[str, Any], None, Unset]
        if isinstance(self.trigger, Unset):
            trigger = UNSET
        elif isinstance(self.trigger, TriggerType0):
            trigger = self.trigger.to_dict()
        else:
            trigger = self.trigger

        triggerer_job: Union[Dict[str, Any], None, Unset]
        if isinstance(self.triggerer_job, Unset):
            triggerer_job = UNSET
        elif isinstance(self.triggerer_job, JobType0):
            triggerer_job = self.triggerer_job.to_dict()
        else:
            triggerer_job = self.triggerer_job

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if task_display_name is not UNSET:
            field_dict["task_display_name"] = task_display_name
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if state is not UNSET:
            field_dict["state"] = state
        if try_number is not UNSET:
            field_dict["try_number"] = try_number
        if map_index is not UNSET:
            field_dict["map_index"] = map_index
        if max_tries is not UNSET:
            field_dict["max_tries"] = max_tries
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if unixname is not UNSET:
            field_dict["unixname"] = unixname
        if pool is not UNSET:
            field_dict["pool"] = pool
        if pool_slots is not UNSET:
            field_dict["pool_slots"] = pool_slots
        if queue is not UNSET:
            field_dict["queue"] = queue
        if priority_weight is not UNSET:
            field_dict["priority_weight"] = priority_weight
        if operator is not UNSET:
            field_dict["operator"] = operator
        if queued_when is not UNSET:
            field_dict["queued_when"] = queued_when
        if pid is not UNSET:
            field_dict["pid"] = pid
        if executor is not UNSET:
            field_dict["executor"] = executor
        if executor_config is not UNSET:
            field_dict["executor_config"] = executor_config
        if sla_miss is not UNSET:
            field_dict["sla_miss"] = sla_miss
        if rendered_map_index is not UNSET:
            field_dict["rendered_map_index"] = rendered_map_index
        if rendered_fields is not UNSET:
            field_dict["rendered_fields"] = rendered_fields
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if triggerer_job is not UNSET:
            field_dict["triggerer_job"] = triggerer_job
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_type_0 import JobType0
        from ..models.sla_miss_type_0 import SLAMissType0
        from ..models.task_instance_rendered_fields import TaskInstanceRenderedFields
        from ..models.trigger_type_0 import TriggerType0

        d = src_dict.copy()
        task_id = d.pop("task_id", UNSET)

        task_display_name = d.pop("task_display_name", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        dag_run_id = d.pop("dag_run_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_state(data: object) -> Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(Union[None, TaskStateType1, TaskStateType2Type1, TaskStateType3Type1, Unset], data)

        state = _parse_state(d.pop("state", UNSET))

        try_number = d.pop("try_number", UNSET)

        map_index = d.pop("map_index", UNSET)

        max_tries = d.pop("max_tries", UNSET)

        hostname = d.pop("hostname", UNSET)

        unixname = d.pop("unixname", UNSET)

        pool = d.pop("pool", UNSET)

        pool_slots = d.pop("pool_slots", UNSET)

        def _parse_queue(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_priority_weight(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        priority_weight = _parse_priority_weight(d.pop("priority_weight", UNSET))

        def _parse_operator(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_queued_when(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        queued_when = _parse_queued_when(d.pop("queued_when", UNSET))

        def _parse_pid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pid = _parse_pid(d.pop("pid", UNSET))

        def _parse_executor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        executor = _parse_executor(d.pop("executor", UNSET))

        executor_config = d.pop("executor_config", UNSET)

        def _parse_sla_miss(data: object) -> Union["SLAMissType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sla_miss_type_0 = SLAMissType0.from_dict(data)

                return componentsschemas_sla_miss_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SLAMissType0", None, Unset], data)

        sla_miss = _parse_sla_miss(d.pop("sla_miss", UNSET))

        def _parse_rendered_map_index(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rendered_map_index = _parse_rendered_map_index(d.pop("rendered_map_index", UNSET))

        _rendered_fields = d.pop("rendered_fields", UNSET)
        rendered_fields: Union[Unset, TaskInstanceRenderedFields]
        if isinstance(_rendered_fields, Unset):
            rendered_fields = UNSET
        else:
            rendered_fields = TaskInstanceRenderedFields.from_dict(_rendered_fields)

        def _parse_trigger(data: object) -> Union["TriggerType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_trigger_type_0 = TriggerType0.from_dict(data)

                return componentsschemas_trigger_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TriggerType0", None, Unset], data)

        trigger = _parse_trigger(d.pop("trigger", UNSET))

        def _parse_triggerer_job(data: object) -> Union["JobType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_job_type_0 = JobType0.from_dict(data)

                return componentsschemas_job_type_0
            except:  # noqa: E722
                pass
            return cast(Union["JobType0", None, Unset], data)

        triggerer_job = _parse_triggerer_job(d.pop("triggerer_job", UNSET))

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        task_instance = cls(
            task_id=task_id,
            task_display_name=task_display_name,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            execution_date=execution_date,
            start_date=start_date,
            end_date=end_date,
            duration=duration,
            state=state,
            try_number=try_number,
            map_index=map_index,
            max_tries=max_tries,
            hostname=hostname,
            unixname=unixname,
            pool=pool,
            pool_slots=pool_slots,
            queue=queue,
            priority_weight=priority_weight,
            operator=operator,
            queued_when=queued_when,
            pid=pid,
            executor=executor,
            executor_config=executor_config,
            sla_miss=sla_miss,
            rendered_map_index=rendered_map_index,
            rendered_fields=rendered_fields,
            trigger=trigger,
            triggerer_job=triggerer_job,
            note=note,
        )

        task_instance.additional_properties = d
        return task_instance

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
