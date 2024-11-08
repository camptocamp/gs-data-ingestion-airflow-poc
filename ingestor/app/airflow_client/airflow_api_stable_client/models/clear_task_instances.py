from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClearTaskInstances")


@_attrs_define
class ClearTaskInstances:
    """
    Attributes:
        dry_run (Union[Unset, bool]): If set, don't actually run this operation. The response will contain a list of
            task instances
            planned to be cleaned, but not modified in any way.
             Default: True.
        task_ids (Union[Unset, List[str]]): A list of task ids to clear.

            *New in version 2.1.0*
        start_date (Union[Unset, str]): The minimum execution date to clear.
        end_date (Union[Unset, str]): The maximum execution date to clear.
        only_failed (Union[Unset, bool]): Only clear failed tasks. Default: True.
        only_running (Union[Unset, bool]): Only clear running tasks. Default: False.
        include_subdags (Union[Unset, bool]): Clear tasks in subdags and clear external tasks indicated by
            ExternalTaskMarker.
        include_parentdag (Union[Unset, bool]): Clear tasks in the parent dag of the subdag.
        reset_dag_runs (Union[Unset, bool]): Set state of DAG runs to RUNNING.
        dag_run_id (Union[None, Unset, str]): The DagRun ID for this task instance
        include_upstream (Union[Unset, bool]): If set to true, upstream tasks are also affected. Default: False.
        include_downstream (Union[Unset, bool]): If set to true, downstream tasks are also affected. Default: False.
        include_future (Union[Unset, bool]): If set to True, also tasks from future DAG Runs are affected. Default:
            False.
        include_past (Union[Unset, bool]): If set to True, also tasks from past DAG Runs are affected. Default: False.
    """

    dry_run: Union[Unset, bool] = True
    task_ids: Union[Unset, List[str]] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    only_failed: Union[Unset, bool] = True
    only_running: Union[Unset, bool] = False
    include_subdags: Union[Unset, bool] = UNSET
    include_parentdag: Union[Unset, bool] = UNSET
    reset_dag_runs: Union[Unset, bool] = UNSET
    dag_run_id: Union[None, Unset, str] = UNSET
    include_upstream: Union[Unset, bool] = False
    include_downstream: Union[Unset, bool] = False
    include_future: Union[Unset, bool] = False
    include_past: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dry_run = self.dry_run

        task_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.task_ids, Unset):
            task_ids = self.task_ids

        start_date = self.start_date

        end_date = self.end_date

        only_failed = self.only_failed

        only_running = self.only_running

        include_subdags = self.include_subdags

        include_parentdag = self.include_parentdag

        reset_dag_runs = self.reset_dag_runs

        dag_run_id: Union[None, Unset, str]
        if isinstance(self.dag_run_id, Unset):
            dag_run_id = UNSET
        else:
            dag_run_id = self.dag_run_id

        include_upstream = self.include_upstream

        include_downstream = self.include_downstream

        include_future = self.include_future

        include_past = self.include_past

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if task_ids is not UNSET:
            field_dict["task_ids"] = task_ids
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if only_failed is not UNSET:
            field_dict["only_failed"] = only_failed
        if only_running is not UNSET:
            field_dict["only_running"] = only_running
        if include_subdags is not UNSET:
            field_dict["include_subdags"] = include_subdags
        if include_parentdag is not UNSET:
            field_dict["include_parentdag"] = include_parentdag
        if reset_dag_runs is not UNSET:
            field_dict["reset_dag_runs"] = reset_dag_runs
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dry_run = d.pop("dry_run", UNSET)

        task_ids = cast(List[str], d.pop("task_ids", UNSET))

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        only_failed = d.pop("only_failed", UNSET)

        only_running = d.pop("only_running", UNSET)

        include_subdags = d.pop("include_subdags", UNSET)

        include_parentdag = d.pop("include_parentdag", UNSET)

        reset_dag_runs = d.pop("reset_dag_runs", UNSET)

        def _parse_dag_run_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dag_run_id = _parse_dag_run_id(d.pop("dag_run_id", UNSET))

        include_upstream = d.pop("include_upstream", UNSET)

        include_downstream = d.pop("include_downstream", UNSET)

        include_future = d.pop("include_future", UNSET)

        include_past = d.pop("include_past", UNSET)

        clear_task_instances = cls(
            dry_run=dry_run,
            task_ids=task_ids,
            start_date=start_date,
            end_date=end_date,
            only_failed=only_failed,
            only_running=only_running,
            include_subdags=include_subdags,
            include_parentdag=include_parentdag,
            reset_dag_runs=reset_dag_runs,
            dag_run_id=dag_run_id,
            include_upstream=include_upstream,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
        )

        clear_task_instances.additional_properties = d
        return clear_task_instances

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
