from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x_com_value_type_5_type_0 import XComValueType5Type0


T = TypeVar("T", bound="XCom")


@_attrs_define
class XCom:
    """Full representations of XCom entry.

    Attributes:
        key (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        execution_date (Union[Unset, str]):
        map_index (Union[Unset, int]):
        task_id (Union[Unset, str]):
        dag_id (Union[Unset, str]):
        value (Union['XComValueType5Type0', List[Any], None, Unset, bool, float, int, str]): The value(s),
    """

    key: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    execution_date: Union[Unset, str] = UNSET
    map_index: Union[Unset, int] = UNSET
    task_id: Union[Unset, str] = UNSET
    dag_id: Union[Unset, str] = UNSET
    value: Union["XComValueType5Type0", List[Any], None, Unset, bool, float, int, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.x_com_value_type_5_type_0 import XComValueType5Type0

        key = self.key

        timestamp = self.timestamp

        execution_date = self.execution_date

        map_index = self.map_index

        task_id = self.task_id

        dag_id = self.dag_id

        value: Union[Dict[str, Any], List[Any], None, Unset, bool, float, int, str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = self.value

        elif isinstance(self.value, XComValueType5Type0):
            value = self.value.to_dict()
        else:
            value = self.value

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
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.x_com_value_type_5_type_0 import XComValueType5Type0

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        map_index = d.pop("map_index", UNSET)

        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        def _parse_value(data: object) -> Union["XComValueType5Type0", List[Any], None, Unset, bool, float, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_4 = cast(List[Any], data)

                return value_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_5_type_0 = XComValueType5Type0.from_dict(data)

                return value_type_5_type_0
            except:  # noqa: E722
                pass
            return cast(Union["XComValueType5Type0", List[Any], None, Unset, bool, float, int, str], data)

        value = _parse_value(d.pop("value", UNSET))

        x_com = cls(
            key=key,
            timestamp=timestamp,
            execution_date=execution_date,
            map_index=map_index,
            task_id=task_id,
            dag_id=dag_id,
            value=value,
        )

        x_com.additional_properties = d
        return x_com

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
