from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag import DAG


T = TypeVar("T", bound="DAGCollection")


@_attrs_define
class DAGCollection:
    """Collection of DAGs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            dags (Union[Unset, List['DAG']]):
    """

    total_entries: Union[Unset, int] = UNSET
    dags: Union[Unset, List["DAG"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        dags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dags, Unset):
            dags = []
            for dags_item_data in self.dags:
                dags_item = dags_item_data.to_dict()
                dags.append(dags_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if dags is not UNSET:
            field_dict["dags"] = dags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dag import DAG

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        dags = []
        _dags = d.pop("dags", UNSET)
        for dags_item_data in _dags or []:
            dags_item = DAG.from_dict(dags_item_data)

            dags.append(dags_item)

        dag_collection = cls(
            total_entries=total_entries,
            dags=dags,
        )

        dag_collection.additional_properties = d
        return dag_collection

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
