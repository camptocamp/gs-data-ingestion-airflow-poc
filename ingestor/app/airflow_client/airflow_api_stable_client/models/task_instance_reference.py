from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskInstanceReference")


@_attrs_define
class TaskInstanceReference:
    """
    Attributes:
        task_id (Union[Unset, str]): The task ID.
        dag_id (Union[Unset, str]): The DAG ID.
        execution_date (Union[Unset, str]):
        dag_run_id (Union[Unset, str]): The DAG run ID.
    """

    task_id: Union[Unset, str] = UNSET
    dag_id: Union[Unset, str] = UNSET
    execution_date: Union[Unset, str] = UNSET
    dag_run_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_id = self.task_id

        dag_id = self.dag_id

        execution_date = self.execution_date

        dag_run_id = self.dag_run_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        dag_run_id = d.pop("dag_run_id", UNSET)

        task_instance_reference = cls(
            task_id=task_id,
            dag_id=dag_id,
            execution_date=execution_date,
            dag_run_id=dag_run_id,
        )

        task_instance_reference.additional_properties = d
        return task_instance_reference

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
