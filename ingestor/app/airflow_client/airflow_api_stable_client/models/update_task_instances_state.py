from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_task_state import UpdateTaskState
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTaskInstancesState")


@_attrs_define
class UpdateTaskInstancesState:
    """
    Attributes:
        dry_run (Union[Unset, bool]): If set, don't actually run this operation. The response will contain a list of
            task instances
            planned to be affected, but won't be modified in any way.
             Default: True.
        task_id (Union[Unset, str]): The task ID.
        execution_date (Union[Unset, str]): The execution date. Either set this or dag_run_id but not both.
        dag_run_id (Union[Unset, str]): The task instance's DAG run ID. Either set this or execution_date but not both.

            *New in version 2.3.0*
        include_upstream (Union[Unset, bool]): If set to true, upstream tasks are also affected.
        include_downstream (Union[Unset, bool]): If set to true, downstream tasks are also affected.
        include_future (Union[Unset, bool]): If set to True, also tasks from future DAG Runs are affected.
        include_past (Union[Unset, bool]): If set to True, also tasks from past DAG Runs are affected.
        new_state (Union[Unset, UpdateTaskState]): Expected new state. Only a subset of TaskState are available.

            Other states are managed directly by the scheduler or the workers and cannot be updated manually through the
            REST API.
    """

    dry_run: Union[Unset, bool] = True
    task_id: Union[Unset, str] = UNSET
    execution_date: Union[Unset, str] = UNSET
    dag_run_id: Union[Unset, str] = UNSET
    include_upstream: Union[Unset, bool] = UNSET
    include_downstream: Union[Unset, bool] = UNSET
    include_future: Union[Unset, bool] = UNSET
    include_past: Union[Unset, bool] = UNSET
    new_state: Union[Unset, UpdateTaskState] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dry_run = self.dry_run

        task_id = self.task_id

        execution_date = self.execution_date

        dag_run_id = self.dag_run_id

        include_upstream = self.include_upstream

        include_downstream = self.include_downstream

        include_future = self.include_future

        include_past = self.include_past

        new_state: Union[Unset, str] = UNSET
        if not isinstance(self.new_state, Unset):
            new_state = self.new_state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if include_upstream is not UNSET:
            field_dict["include_upstream"] = include_upstream
        if include_downstream is not UNSET:
            field_dict["include_downstream"] = include_downstream
        if include_future is not UNSET:
            field_dict["include_future"] = include_future
        if include_past is not UNSET:
            field_dict["include_past"] = include_past
        if new_state is not UNSET:
            field_dict["new_state"] = new_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dry_run = d.pop("dry_run", UNSET)

        task_id = d.pop("task_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        dag_run_id = d.pop("dag_run_id", UNSET)

        include_upstream = d.pop("include_upstream", UNSET)

        include_downstream = d.pop("include_downstream", UNSET)

        include_future = d.pop("include_future", UNSET)

        include_past = d.pop("include_past", UNSET)

        _new_state = d.pop("new_state", UNSET)
        new_state: Union[Unset, UpdateTaskState]
        if isinstance(_new_state, Unset):
            new_state = UNSET
        else:
            new_state = UpdateTaskState(_new_state)

        update_task_instances_state = cls(
            dry_run=dry_run,
            task_id=task_id,
            execution_date=execution_date,
            dag_run_id=dag_run_id,
            include_upstream=include_upstream,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
            new_state=new_state,
        )

        update_task_instances_state.additional_properties = d
        return update_task_instances_state

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
