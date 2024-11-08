from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SLAMissType0")


@_attrs_define
class SLAMissType0:
    """
    Attributes:
        task_id (Union[Unset, str]): The task ID.
        dag_id (Union[Unset, str]): The DAG ID.
        execution_date (Union[Unset, str]):
        email_sent (Union[Unset, bool]):
        timestamp (Union[Unset, str]):
        description (Union[None, Unset, str]):
        notification_sent (Union[Unset, bool]):
    """

    task_id: Union[Unset, str] = UNSET
    dag_id: Union[Unset, str] = UNSET
    execution_date: Union[Unset, str] = UNSET
    email_sent: Union[Unset, bool] = UNSET
    timestamp: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    notification_sent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_id = self.task_id

        dag_id = self.dag_id

        execution_date = self.execution_date

        email_sent = self.email_sent

        timestamp = self.timestamp

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        notification_sent = self.notification_sent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if email_sent is not UNSET:
            field_dict["email_sent"] = email_sent
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if notification_sent is not UNSET:
            field_dict["notification_sent"] = notification_sent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        email_sent = d.pop("email_sent", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        notification_sent = d.pop("notification_sent", UNSET)

        sla_miss_type_0 = cls(
            task_id=task_id,
            dag_id=dag_id,
            execution_date=execution_date,
            email_sent=email_sent,
            timestamp=timestamp,
            description=description,
            notification_sent=notification_sent,
        )

        sla_miss_type_0.additional_properties = d
        return sla_miss_type_0

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
