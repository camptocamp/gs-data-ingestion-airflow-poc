from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DagScheduleDatasetReference")


@_attrs_define
class DagScheduleDatasetReference:
    """A datasets reference to a downstream DAG.

    *New in version 2.4.0*

        Attributes:
            dag_id (Union[None, Unset, str]): The DAG ID that depends on the dataset.
            created_at (Union[Unset, str]): The dataset reference creation time
            updated_at (Union[Unset, str]): The dataset reference update time
    """

    dag_id: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dag_id: Union[None, Unset, str]
        if isinstance(self.dag_id, Unset):
            dag_id = UNSET
        else:
            dag_id = self.dag_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_dag_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dag_id = _parse_dag_id(d.pop("dag_id", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        dag_schedule_dataset_reference = cls(
            dag_id=dag_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        dag_schedule_dataset_reference.additional_properties = d
        return dag_schedule_dataset_reference

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
