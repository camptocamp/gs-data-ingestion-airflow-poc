from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_task_state import UpdateTaskState
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTaskInstance")


@_attrs_define
class UpdateTaskInstance:
    """
    Attributes:
        dry_run (Union[Unset, bool]): If set, don't actually run this operation. The response will contain the task
            instance
            planned to be affected, but won't be modified in any way.
             Default: True.
        new_state (Union[Unset, UpdateTaskState]): Expected new state. Only a subset of TaskState are available.

            Other states are managed directly by the scheduler or the workers and cannot be updated manually through the
            REST API.
    """

    dry_run: Union[Unset, bool] = True
    new_state: Union[Unset, UpdateTaskState] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dry_run = self.dry_run

        new_state: Union[Unset, str] = UNSET
        if not isinstance(self.new_state, Unset):
            new_state = self.new_state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if new_state is not UNSET:
            field_dict["new_state"] = new_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dry_run = d.pop("dry_run", UNSET)

        _new_state = d.pop("new_state", UNSET)
        new_state: Union[Unset, UpdateTaskState]
        if isinstance(_new_state, Unset):
            new_state = UNSET
        else:
            new_state = UpdateTaskState(_new_state)

        update_task_instance = cls(
            dry_run=dry_run,
            new_state=new_state,
        )

        update_task_instance.additional_properties = d
        return update_task_instance

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
