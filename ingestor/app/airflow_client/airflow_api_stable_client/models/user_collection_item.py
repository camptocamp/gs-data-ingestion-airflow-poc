from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_collection_item_roles_item_type_0 import UserCollectionItemRolesItemType0


T = TypeVar("T", bound="UserCollectionItem")


@_attrs_define
class UserCollectionItem:
    """A user object.

    *New in version 2.1.0*

        Attributes:
            first_name (Union[Unset, str]): The user's first name.

                *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.
            last_name (Union[Unset, str]): The user's last name.

                *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.
            username (Union[Unset, str]): The username.

                *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.
            email (Union[Unset, str]): The user's email.

                *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.
            active (Union[None, Unset, bool]): Whether the user is active
            last_login (Union[None, Unset, str]): The last user login
            login_count (Union[None, Unset, int]): The login count
            failed_login_count (Union[None, Unset, int]): The number of times the login failed
            roles (Union[Unset, List[Union['UserCollectionItemRolesItemType0', None]]]): User roles.

                *Changed in version 2.2.0*&#58; Field is no longer read-only.
            created_on (Union[None, Unset, str]): The date user was created
            changed_on (Union[None, Unset, str]): The date user was changed
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    active: Union[None, Unset, bool] = UNSET
    last_login: Union[None, Unset, str] = UNSET
    login_count: Union[None, Unset, int] = UNSET
    failed_login_count: Union[None, Unset, int] = UNSET
    roles: Union[Unset, List[Union["UserCollectionItemRolesItemType0", None]]] = UNSET
    created_on: Union[None, Unset, str] = UNSET
    changed_on: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.user_collection_item_roles_item_type_0 import UserCollectionItemRolesItemType0

        first_name = self.first_name

        last_name = self.last_name

        username = self.username

        email = self.email

        active: Union[None, Unset, bool]
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        last_login: Union[None, Unset, str]
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        else:
            last_login = self.last_login

        login_count: Union[None, Unset, int]
        if isinstance(self.login_count, Unset):
            login_count = UNSET
        else:
            login_count = self.login_count

        failed_login_count: Union[None, Unset, int]
        if isinstance(self.failed_login_count, Unset):
            failed_login_count = UNSET
        else:
            failed_login_count = self.failed_login_count

        roles: Union[Unset, List[Union[Dict[str, Any], None]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item: Union[Dict[str, Any], None]
                if isinstance(roles_item_data, UserCollectionItemRolesItemType0):
                    roles_item = roles_item_data.to_dict()
                else:
                    roles_item = roles_item_data
                roles.append(roles_item)

        created_on: Union[None, Unset, str]
        if isinstance(self.created_on, Unset):
            created_on = UNSET
        else:
            created_on = self.created_on

        changed_on: Union[None, Unset, str]
        if isinstance(self.changed_on, Unset):
            changed_on = UNSET
        else:
            changed_on = self.changed_on

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if active is not UNSET:
            field_dict["active"] = active
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if login_count is not UNSET:
            field_dict["login_count"] = login_count
        if failed_login_count is not UNSET:
            field_dict["failed_login_count"] = failed_login_count
        if roles is not UNSET:
            field_dict["roles"] = roles
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if changed_on is not UNSET:
            field_dict["changed_on"] = changed_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_collection_item_roles_item_type_0 import UserCollectionItemRolesItemType0

        d = src_dict.copy()
        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        def _parse_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_last_login(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_login = _parse_last_login(d.pop("last_login", UNSET))

        def _parse_login_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        login_count = _parse_login_count(d.pop("login_count", UNSET))

        def _parse_failed_login_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        failed_login_count = _parse_failed_login_count(d.pop("failed_login_count", UNSET))

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:

            def _parse_roles_item(data: object) -> Union["UserCollectionItemRolesItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    roles_item_type_0 = UserCollectionItemRolesItemType0.from_dict(data)

                    return roles_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["UserCollectionItemRolesItemType0", None], data)

            roles_item = _parse_roles_item(roles_item_data)

            roles.append(roles_item)

        def _parse_created_on(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_on = _parse_created_on(d.pop("created_on", UNSET))

        def _parse_changed_on(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        changed_on = _parse_changed_on(d.pop("changed_on", UNSET))

        user_collection_item = cls(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            active=active,
            last_login=last_login,
            login_count=login_count,
            failed_login_count=failed_login_count,
            roles=roles,
            created_on=created_on,
            changed_on=changed_on,
        )

        user_collection_item.additional_properties = d
        return user_collection_item

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
