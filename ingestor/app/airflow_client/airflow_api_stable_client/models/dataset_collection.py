from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset import Dataset


T = TypeVar("T", bound="DatasetCollection")


@_attrs_define
class DatasetCollection:
    """A collection of datasets.

    *New in version 2.4.0*

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            datasets (Union[Unset, List['Dataset']]):
    """

    total_entries: Union[Unset, int] = UNSET
    datasets: Union[Unset, List["Dataset"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        datasets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset import Dataset

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = Dataset.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        dataset_collection = cls(
            total_entries=total_entries,
            datasets=datasets,
        )

        dataset_collection.additional_properties = d
        return dataset_collection

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
