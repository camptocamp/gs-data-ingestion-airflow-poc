from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider import Provider


T = TypeVar("T", bound="ProviderCollection")


@_attrs_define
class ProviderCollection:
    """Collection of providers.

    *New in version 2.1.0*

        Attributes:
            providers (Union[Unset, List['Provider']]):
    """

    providers: Union[Unset, List["Provider"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provider import Provider

        d = src_dict.copy()
        providers = []
        _providers = d.pop("providers", UNSET)
        for providers_item_data in _providers or []:
            providers_item = Provider.from_dict(providers_item_data)

            providers.append(providers_item)

        provider_collection = cls(
            providers=providers,
        )

        provider_collection.additional_properties = d
        return provider_collection

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
