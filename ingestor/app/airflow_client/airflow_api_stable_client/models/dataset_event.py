from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_dag_run import BasicDAGRun
    from ..models.dataset_event_extra_type_0 import DatasetEventExtraType0


T = TypeVar("T", bound="DatasetEvent")


@_attrs_define
class DatasetEvent:
    """A dataset event.

    *New in version 2.4.0*

        Attributes:
            dataset_id (Union[Unset, int]): The dataset id
            dataset_uri (Union[Unset, str]): The URI of the dataset
            extra (Union['DatasetEventExtraType0', None, Unset]): The dataset event extra
            source_dag_id (Union[None, Unset, str]): The DAG ID that updated the dataset.
            source_task_id (Union[None, Unset, str]): The task ID that updated the dataset.
            source_run_id (Union[None, Unset, str]): The DAG run ID that updated the dataset.
            source_map_index (Union[None, Unset, int]): The task map index that updated the dataset.
            created_dagruns (Union[Unset, List['BasicDAGRun']]):
            timestamp (Union[Unset, str]): The dataset event creation time
    """

    dataset_id: Union[Unset, int] = UNSET
    dataset_uri: Union[Unset, str] = UNSET
    extra: Union["DatasetEventExtraType0", None, Unset] = UNSET
    source_dag_id: Union[None, Unset, str] = UNSET
    source_task_id: Union[None, Unset, str] = UNSET
    source_run_id: Union[None, Unset, str] = UNSET
    source_map_index: Union[None, Unset, int] = UNSET
    created_dagruns: Union[Unset, List["BasicDAGRun"]] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dataset_event_extra_type_0 import DatasetEventExtraType0

        dataset_id = self.dataset_id

        dataset_uri = self.dataset_uri

        extra: Union[Dict[str, Any], None, Unset]
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, DatasetEventExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        source_dag_id: Union[None, Unset, str]
        if isinstance(self.source_dag_id, Unset):
            source_dag_id = UNSET
        else:
            source_dag_id = self.source_dag_id

        source_task_id: Union[None, Unset, str]
        if isinstance(self.source_task_id, Unset):
            source_task_id = UNSET
        else:
            source_task_id = self.source_task_id

        source_run_id: Union[None, Unset, str]
        if isinstance(self.source_run_id, Unset):
            source_run_id = UNSET
        else:
            source_run_id = self.source_run_id

        source_map_index: Union[None, Unset, int]
        if isinstance(self.source_map_index, Unset):
            source_map_index = UNSET
        else:
            source_map_index = self.source_map_index

        created_dagruns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.created_dagruns, Unset):
            created_dagruns = []
            for created_dagruns_item_data in self.created_dagruns:
                created_dagruns_item = created_dagruns_item_data.to_dict()
                created_dagruns.append(created_dagruns_item)

        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if dataset_uri is not UNSET:
            field_dict["dataset_uri"] = dataset_uri
        if extra is not UNSET:
            field_dict["extra"] = extra
        if source_dag_id is not UNSET:
            field_dict["source_dag_id"] = source_dag_id
        if source_task_id is not UNSET:
            field_dict["source_task_id"] = source_task_id
        if source_run_id is not UNSET:
            field_dict["source_run_id"] = source_run_id
        if source_map_index is not UNSET:
            field_dict["source_map_index"] = source_map_index
        if created_dagruns is not UNSET:
            field_dict["created_dagruns"] = created_dagruns
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_dag_run import BasicDAGRun
        from ..models.dataset_event_extra_type_0 import DatasetEventExtraType0

        d = src_dict.copy()
        dataset_id = d.pop("dataset_id", UNSET)

        dataset_uri = d.pop("dataset_uri", UNSET)

        def _parse_extra(data: object) -> Union["DatasetEventExtraType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = DatasetEventExtraType0.from_dict(data)

                return extra_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DatasetEventExtraType0", None, Unset], data)

        extra = _parse_extra(d.pop("extra", UNSET))

        def _parse_source_dag_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_dag_id = _parse_source_dag_id(d.pop("source_dag_id", UNSET))

        def _parse_source_task_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_task_id = _parse_source_task_id(d.pop("source_task_id", UNSET))

        def _parse_source_run_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_run_id = _parse_source_run_id(d.pop("source_run_id", UNSET))

        def _parse_source_map_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_map_index = _parse_source_map_index(d.pop("source_map_index", UNSET))

        created_dagruns = []
        _created_dagruns = d.pop("created_dagruns", UNSET)
        for created_dagruns_item_data in _created_dagruns or []:
            created_dagruns_item = BasicDAGRun.from_dict(created_dagruns_item_data)

            created_dagruns.append(created_dagruns_item)

        timestamp = d.pop("timestamp", UNSET)

        dataset_event = cls(
            dataset_id=dataset_id,
            dataset_uri=dataset_uri,
            extra=extra,
            source_dag_id=source_dag_id,
            source_task_id=source_task_id,
            source_run_id=source_run_id,
            source_map_index=source_map_index,
            created_dagruns=created_dagruns,
            timestamp=timestamp,
        )

        dataset_event.additional_properties = d
        return dataset_event

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
