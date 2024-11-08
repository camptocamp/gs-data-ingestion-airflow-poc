from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_failed_dependency import TaskFailedDependency


T = TypeVar("T", bound="TaskInstanceDependencyCollection")


@_attrs_define
class TaskInstanceDependencyCollection:
    """
    Attributes:
        dependencies (Union[Unset, List['TaskFailedDependency']]):
    """

    dependencies: Union[Unset, List["TaskFailedDependency"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dependencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_failed_dependency import TaskFailedDependency

        d = src_dict.copy()
        dependencies = []
        _dependencies = d.pop("dependencies", UNSET)
        for dependencies_item_data in _dependencies or []:
            dependencies_item = TaskFailedDependency.from_dict(dependencies_item_data)

            dependencies.append(dependencies_item)

        task_instance_dependency_collection = cls(
            dependencies=dependencies,
        )

        task_instance_dependency_collection.additional_properties = d
        return task_instance_dependency_collection

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
