from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_instance import TaskInstance


T = TypeVar("T", bound="TaskInstanceCollection")


@_attrs_define
class TaskInstanceCollection:
    """Collection of task instances.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            task_instances (Union[Unset, List['TaskInstance']]):
    """

    total_entries: Union[Unset, int] = UNSET
    task_instances: Union[Unset, List["TaskInstance"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        task_instances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.task_instances, Unset):
            task_instances = []
            for task_instances_item_data in self.task_instances:
                task_instances_item = task_instances_item_data.to_dict()
                task_instances.append(task_instances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if task_instances is not UNSET:
            field_dict["task_instances"] = task_instances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_instance import TaskInstance

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        task_instances = []
        _task_instances = d.pop("task_instances", UNSET)
        for task_instances_item_data in _task_instances or []:
            task_instances_item = TaskInstance.from_dict(task_instances_item_data)

            task_instances.append(task_instances_item)

        task_instance_collection = cls(
            total_entries=total_entries,
            task_instances=task_instances,
        )

        task_instance_collection.additional_properties = d
        return task_instance_collection

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
