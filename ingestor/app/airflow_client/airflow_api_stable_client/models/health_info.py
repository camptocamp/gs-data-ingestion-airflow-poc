from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_processor_status import DagProcessorStatus
    from ..models.metadatabase_status import MetadatabaseStatus
    from ..models.scheduler_status import SchedulerStatus
    from ..models.triggerer_status import TriggererStatus


T = TypeVar("T", bound="HealthInfo")


@_attrs_define
class HealthInfo:
    """Instance status information.

    Attributes:
        metadatabase (Union[Unset, MetadatabaseStatus]): The status of the metadatabase.
        scheduler (Union[Unset, SchedulerStatus]): The status and the latest scheduler heartbeat.
        triggerer (Union[Unset, TriggererStatus]): The status and the latest triggerer heartbeat.

            *New in version 2.6.2*
        dag_processor (Union[Unset, DagProcessorStatus]): The status and the latest dag processor heartbeat.

            *New in version 2.6.3*
    """

    metadatabase: Union[Unset, "MetadatabaseStatus"] = UNSET
    scheduler: Union[Unset, "SchedulerStatus"] = UNSET
    triggerer: Union[Unset, "TriggererStatus"] = UNSET
    dag_processor: Union[Unset, "DagProcessorStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadatabase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadatabase, Unset):
            metadatabase = self.metadatabase.to_dict()

        scheduler: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.to_dict()

        triggerer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.triggerer, Unset):
            triggerer = self.triggerer.to_dict()

        dag_processor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dag_processor, Unset):
            dag_processor = self.dag_processor.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadatabase is not UNSET:
            field_dict["metadatabase"] = metadatabase
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if triggerer is not UNSET:
            field_dict["triggerer"] = triggerer
        if dag_processor is not UNSET:
            field_dict["dag_processor"] = dag_processor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dag_processor_status import DagProcessorStatus
        from ..models.metadatabase_status import MetadatabaseStatus
        from ..models.scheduler_status import SchedulerStatus
        from ..models.triggerer_status import TriggererStatus

        d = src_dict.copy()
        _metadatabase = d.pop("metadatabase", UNSET)
        metadatabase: Union[Unset, MetadatabaseStatus]
        if isinstance(_metadatabase, Unset):
            metadatabase = UNSET
        else:
            metadatabase = MetadatabaseStatus.from_dict(_metadatabase)

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: Union[Unset, SchedulerStatus]
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = SchedulerStatus.from_dict(_scheduler)

        _triggerer = d.pop("triggerer", UNSET)
        triggerer: Union[Unset, TriggererStatus]
        if isinstance(_triggerer, Unset):
            triggerer = UNSET
        else:
            triggerer = TriggererStatus.from_dict(_triggerer)

        _dag_processor = d.pop("dag_processor", UNSET)
        dag_processor: Union[Unset, DagProcessorStatus]
        if isinstance(_dag_processor, Unset):
            dag_processor = UNSET
        else:
            dag_processor = DagProcessorStatus.from_dict(_dag_processor)

        health_info = cls(
            metadatabase=metadatabase,
            scheduler=scheduler,
            triggerer=triggerer,
            dag_processor=dag_processor,
        )

        health_info.additional_properties = d
        return health_info

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
