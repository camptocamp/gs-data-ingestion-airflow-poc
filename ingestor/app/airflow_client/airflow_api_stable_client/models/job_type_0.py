from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobType0")


@_attrs_define
class JobType0:
    """
    Attributes:
        id (Union[Unset, int]):
        dag_id (Union[None, Unset, str]):
        state (Union[None, Unset, str]):
        job_type (Union[None, Unset, str]):
        start_date (Union[None, Unset, str]):
        end_date (Union[None, Unset, str]):
        latest_heartbeat (Union[None, Unset, str]):
        executor_class (Union[None, Unset, str]):
        hostname (Union[None, Unset, str]):
        unixname (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    dag_id: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    job_type: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    latest_heartbeat: Union[None, Unset, str] = UNSET
    executor_class: Union[None, Unset, str] = UNSET
    hostname: Union[None, Unset, str] = UNSET
    unixname: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        dag_id: Union[None, Unset, str]
        if isinstance(self.dag_id, Unset):
            dag_id = UNSET
        else:
            dag_id = self.dag_id

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        job_type: Union[None, Unset, str]
        if isinstance(self.job_type, Unset):
            job_type = UNSET
        else:
            job_type = self.job_type

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        latest_heartbeat: Union[None, Unset, str]
        if isinstance(self.latest_heartbeat, Unset):
            latest_heartbeat = UNSET
        else:
            latest_heartbeat = self.latest_heartbeat

        executor_class: Union[None, Unset, str]
        if isinstance(self.executor_class, Unset):
            executor_class = UNSET
        else:
            executor_class = self.executor_class

        hostname: Union[None, Unset, str]
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        unixname: Union[None, Unset, str]
        if isinstance(self.unixname, Unset):
            unixname = UNSET
        else:
            unixname = self.unixname

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if state is not UNSET:
            field_dict["state"] = state
        if job_type is not UNSET:
            field_dict["job_type"] = job_type
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if latest_heartbeat is not UNSET:
            field_dict["latest_heartbeat"] = latest_heartbeat
        if executor_class is not UNSET:
            field_dict["executor_class"] = executor_class
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if unixname is not UNSET:
            field_dict["unixname"] = unixname

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_dag_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dag_id = _parse_dag_id(d.pop("dag_id", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_job_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_type = _parse_job_type(d.pop("job_type", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_latest_heartbeat(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        latest_heartbeat = _parse_latest_heartbeat(d.pop("latest_heartbeat", UNSET))

        def _parse_executor_class(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        executor_class = _parse_executor_class(d.pop("executor_class", UNSET))

        def _parse_hostname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_unixname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unixname = _parse_unixname(d.pop("unixname", UNSET))

        job_type_0 = cls(
            id=id,
            dag_id=dag_id,
            state=state,
            job_type=job_type,
            start_date=start_date,
            end_date=end_date,
            latest_heartbeat=latest_heartbeat,
            executor_class=executor_class,
            hostname=hostname,
            unixname=unixname,
        )

        job_type_0.additional_properties = d
        return job_type_0

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
