from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_instance_reference import TaskInstanceReference


T = TypeVar("T", bound="TaskInstanceReferenceCollection")


@_attrs_define
class TaskInstanceReferenceCollection:
    """
    Attributes:
        task_instances (Union[Unset, List['TaskInstanceReference']]):
    """

    task_instances: Union[Unset, List["TaskInstanceReference"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_instances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.task_instances, Unset):
            task_instances = []
            for task_instances_item_data in self.task_instances:
                task_instances_item = task_instances_item_data.to_dict()
                task_instances.append(task_instances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_instances is not UNSET:
            field_dict["task_instances"] = task_instances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_instance_reference import TaskInstanceReference

        d = src_dict.copy()
        task_instances = []
        _task_instances = d.pop("task_instances", UNSET)
        for task_instances_item_data in _task_instances or []:
            task_instances_item = TaskInstanceReference.from_dict(task_instances_item_data)

            task_instances.append(task_instances_item)

        task_instance_reference_collection = cls(
            task_instances=task_instances,
        )

        task_instance_reference_collection.additional_properties = d
        return task_instance_reference_collection

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
