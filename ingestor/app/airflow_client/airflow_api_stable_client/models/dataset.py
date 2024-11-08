from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_schedule_dataset_reference import DagScheduleDatasetReference
    from ..models.dataset_extra_type_0 import DatasetExtraType0
    from ..models.task_outlet_dataset_reference import TaskOutletDatasetReference


T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """A dataset item.

    *New in version 2.4.0*

        Attributes:
            id (Union[Unset, int]): The dataset id
            uri (Union[Unset, str]): The dataset uri
            extra (Union['DatasetExtraType0', None, Unset]): The dataset extra
            created_at (Union[Unset, str]): The dataset creation time
            updated_at (Union[Unset, str]): The dataset update time
            consuming_dags (Union[Unset, List['DagScheduleDatasetReference']]):
            producing_tasks (Union[Unset, List['TaskOutletDatasetReference']]):
    """

    id: Union[Unset, int] = UNSET
    uri: Union[Unset, str] = UNSET
    extra: Union["DatasetExtraType0", None, Unset] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    consuming_dags: Union[Unset, List["DagScheduleDatasetReference"]] = UNSET
    producing_tasks: Union[Unset, List["TaskOutletDatasetReference"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dataset_extra_type_0 import DatasetExtraType0

        id = self.id

        uri = self.uri

        extra: Union[Dict[str, Any], None, Unset]
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, DatasetExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        created_at = self.created_at

        updated_at = self.updated_at

        consuming_dags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.consuming_dags, Unset):
            consuming_dags = []
            for consuming_dags_item_data in self.consuming_dags:
                consuming_dags_item = consuming_dags_item_data.to_dict()
                consuming_dags.append(consuming_dags_item)

        producing_tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.producing_tasks, Unset):
            producing_tasks = []
            for producing_tasks_item_data in self.producing_tasks:
                producing_tasks_item = producing_tasks_item_data.to_dict()
                producing_tasks.append(producing_tasks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uri is not UNSET:
            field_dict["uri"] = uri
        if extra is not UNSET:
            field_dict["extra"] = extra
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if consuming_dags is not UNSET:
            field_dict["consuming_dags"] = consuming_dags
        if producing_tasks is not UNSET:
            field_dict["producing_tasks"] = producing_tasks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dag_schedule_dataset_reference import DagScheduleDatasetReference
        from ..models.dataset_extra_type_0 import DatasetExtraType0
        from ..models.task_outlet_dataset_reference import TaskOutletDatasetReference

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uri = d.pop("uri", UNSET)

        def _parse_extra(data: object) -> Union["DatasetExtraType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = DatasetExtraType0.from_dict(data)

                return extra_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DatasetExtraType0", None, Unset], data)

        extra = _parse_extra(d.pop("extra", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        consuming_dags = []
        _consuming_dags = d.pop("consuming_dags", UNSET)
        for consuming_dags_item_data in _consuming_dags or []:
            consuming_dags_item = DagScheduleDatasetReference.from_dict(consuming_dags_item_data)

            consuming_dags.append(consuming_dags_item)

        producing_tasks = []
        _producing_tasks = d.pop("producing_tasks", UNSET)
        for producing_tasks_item_data in _producing_tasks or []:
            producing_tasks_item = TaskOutletDatasetReference.from_dict(producing_tasks_item_data)

            producing_tasks.append(producing_tasks_item)

        dataset = cls(
            id=id,
            uri=uri,
            extra=extra,
            created_at=created_at,
            updated_at=updated_at,
            consuming_dags=consuming_dags,
            producing_tasks=producing_tasks,
        )

        dataset.additional_properties = d
        return dataset

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
