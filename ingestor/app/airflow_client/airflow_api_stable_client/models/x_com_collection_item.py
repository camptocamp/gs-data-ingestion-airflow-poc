from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XComCollectionItem")


@_attrs_define
class XComCollectionItem:
    """XCom entry collection item.

    The value field is only available when reading a single object due to the size of the value.

        Attributes:
            key (Union[Unset, str]):
            timestamp (Union[Unset, str]):
            execution_date (Union[Unset, str]):
            map_index (Union[Unset, int]):
            task_id (Union[Unset, str]):
            dag_id (Union[Unset, str]):
    """

    key: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    execution_date: Union[Unset, str] = UNSET
    map_index: Union[Unset, int] = UNSET
    task_id: Union[Unset, str] = UNSET
    dag_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        timestamp = self.timestamp

        execution_date = self.execution_date

        map_index = self.map_index

        task_id = self.task_id

        dag_id = self.dag_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if map_index is not UNSET:
            field_dict["map_index"] = map_index
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        map_index = d.pop("map_index", UNSET)

        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        x_com_collection_item = cls(
            key=key,
            timestamp=timestamp,
            execution_date=execution_date,
            map_index=map_index,
            task_id=task_id,
            dag_id=dag_id,
        )

        x_com_collection_item.additional_properties = d
        return x_com_collection_item

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
