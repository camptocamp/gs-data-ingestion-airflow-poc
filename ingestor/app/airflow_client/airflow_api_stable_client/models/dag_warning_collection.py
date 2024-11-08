from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_warning import DagWarning


T = TypeVar("T", bound="DagWarningCollection")


@_attrs_define
class DagWarningCollection:
    """Collection of DAG warnings.

    Attributes:
        total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
            (limit, offset) are applied.
        dag_warnings (Union[Unset, List['DagWarning']]):
    """

    total_entries: Union[Unset, int] = UNSET
    dag_warnings: Union[Unset, List["DagWarning"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        dag_warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dag_warnings, Unset):
            dag_warnings = []
            for dag_warnings_item_data in self.dag_warnings:
                dag_warnings_item = dag_warnings_item_data.to_dict()
                dag_warnings.append(dag_warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if dag_warnings is not UNSET:
            field_dict["dag_warnings"] = dag_warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dag_warning import DagWarning

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        dag_warnings = []
        _dag_warnings = d.pop("dag_warnings", UNSET)
        for dag_warnings_item_data in _dag_warnings or []:
            dag_warnings_item = DagWarning.from_dict(dag_warnings_item_data)

            dag_warnings.append(dag_warnings_item)

        dag_warning_collection = cls(
            total_entries=total_entries,
            dag_warnings=dag_warnings,
        )

        dag_warning_collection.additional_properties = d
        return dag_warning_collection

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
