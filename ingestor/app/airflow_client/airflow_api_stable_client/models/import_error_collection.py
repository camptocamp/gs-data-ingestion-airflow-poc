from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_error import ImportError_


T = TypeVar("T", bound="ImportErrorCollection")


@_attrs_define
class ImportErrorCollection:
    """Collection of import errors.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            import_errors (Union[Unset, List['ImportError_']]):
    """

    total_entries: Union[Unset, int] = UNSET
    import_errors: Union[Unset, List["ImportError_"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        import_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.import_errors, Unset):
            import_errors = []
            for import_errors_item_data in self.import_errors:
                import_errors_item = import_errors_item_data.to_dict()
                import_errors.append(import_errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if import_errors is not UNSET:
            field_dict["import_errors"] = import_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.import_error import ImportError_

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        import_errors = []
        _import_errors = d.pop("import_errors", UNSET)
        for import_errors_item_data in _import_errors or []:
            import_errors_item = ImportError_.from_dict(import_errors_item_data)

            import_errors.append(import_errors_item)

        import_error_collection = cls(
            total_entries=total_entries,
            import_errors=import_errors,
        )

        import_error_collection.additional_properties = d
        return import_error_collection

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
