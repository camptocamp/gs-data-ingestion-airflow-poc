from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dag_run_state_state import UpdateDagRunStateState
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDagRunState")


@_attrs_define
class UpdateDagRunState:
    """Modify the state of a DAG run.

    *New in version 2.2.0*

        Attributes:
            state (Union[Unset, UpdateDagRunStateState]): The state to set this DagRun
    """

    state: Union[Unset, UpdateDagRunStateState] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, UpdateDagRunStateState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = UpdateDagRunStateState(_state)

        update_dag_run_state = cls(
            state=state,
        )

        update_dag_run_state.additional_properties = d
        return update_dag_run_state

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
