from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_resource_action import ActionResourceAction
    from ..models.action_resource_resource import ActionResourceResource


T = TypeVar("T", bound="ActionResource")


@_attrs_define
class ActionResource:
    """The Action-Resource item.

    *New in version 2.1.0*

        Attributes:
            action (Union[Unset, ActionResourceAction]): The permission action
            resource (Union[Unset, ActionResourceResource]): The permission resource
    """

    action: Union[Unset, "ActionResourceAction"] = UNSET
    resource: Union[Unset, "ActionResourceResource"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_resource_action import ActionResourceAction
        from ..models.action_resource_resource import ActionResourceResource

        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, ActionResourceAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ActionResourceAction.from_dict(_action)

        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, ActionResourceResource]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = ActionResourceResource.from_dict(_resource)

        action_resource = cls(
            action=action,
            resource=resource,
        )

        action_resource.additional_properties = d
        return action_resource

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
