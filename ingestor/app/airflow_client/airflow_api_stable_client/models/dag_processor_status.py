from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_status import HealthStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DagProcessorStatus")


@_attrs_define
class DagProcessorStatus:
    """The status and the latest dag processor heartbeat.

    *New in version 2.6.3*

        Attributes:
            status (Union[Unset, HealthStatus]): Health status
            latest_dag_processor_heartbeat (Union[None, Unset, str]): The time the dag processor last did a heartbeat.
    """

    status: Union[Unset, HealthStatus] = UNSET
    latest_dag_processor_heartbeat: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        latest_dag_processor_heartbeat: Union[None, Unset, str]
        if isinstance(self.latest_dag_processor_heartbeat, Unset):
            latest_dag_processor_heartbeat = UNSET
        else:
            latest_dag_processor_heartbeat = self.latest_dag_processor_heartbeat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if latest_dag_processor_heartbeat is not UNSET:
            field_dict["latest_dag_processor_heartbeat"] = latest_dag_processor_heartbeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, HealthStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HealthStatus(_status)

        def _parse_latest_dag_processor_heartbeat(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        latest_dag_processor_heartbeat = _parse_latest_dag_processor_heartbeat(
            d.pop("latest_dag_processor_heartbeat", UNSET)
        )

        dag_processor_status = cls(
            status=status,
            latest_dag_processor_heartbeat=latest_dag_processor_heartbeat,
        )

        dag_processor_status.additional_properties = d
        return dag_processor_status

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
