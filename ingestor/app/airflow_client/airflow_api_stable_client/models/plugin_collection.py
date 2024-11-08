from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_collection_item import PluginCollectionItem


T = TypeVar("T", bound="PluginCollection")


@_attrs_define
class PluginCollection:
    """A collection of plugin.

    *New in version 2.1.0*

        Attributes:
            total_entries (Union[Unset, int]): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            plugins (Union[Unset, List['PluginCollectionItem']]):
    """

    total_entries: Union[Unset, int] = UNSET
    plugins: Union[Unset, List["PluginCollectionItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        plugins: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = []
            for plugins_item_data in self.plugins:
                plugins_item = plugins_item_data.to_dict()
                plugins.append(plugins_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if plugins is not UNSET:
            field_dict["plugins"] = plugins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin_collection_item import PluginCollectionItem

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        plugins = []
        _plugins = d.pop("plugins", UNSET)
        for plugins_item_data in _plugins or []:
            plugins_item = PluginCollectionItem.from_dict(plugins_item_data)

            plugins.append(plugins_item)

        plugin_collection = cls(
            total_entries=total_entries,
            plugins=plugins,
        )

        plugin_collection.additional_properties = d
        return plugin_collection

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
