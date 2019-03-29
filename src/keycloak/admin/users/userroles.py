import json

from keycloak.admin import KeycloakAdminBase

__all__ = ('UserRoleMappings','UserRoleMappingsRealm')


class UserRoleMappings(KeycloakAdminBase):

    def __init__(self, realm_name, user_id, *args, **kwargs):
        self._realm_name = realm_name
        self._user_id = user_id
        super(UserRoleMappings, self).__init__(*args, **kwargs)

    @property
    def realm(self):
        return UserRoleMappingsRealm(
            realm_name=self._realm_name,
            user_id=self._user_id,
            client=self._client
        )


class UserRoleMappingsRealm(KeycloakAdminBase):
    _paths = {
        'available': '/auth/admin/realms/{realm}/users/{id}' +
                     '/role-mappings/realm/available',
        'single': '/auth/admin/realms/{realm}/users/{id}' +
                  '/role-mappings/realm'
    }

    def __init__(self, realm_name, user_id, *args, **kwargs):
        self._realm_name = realm_name
        self._user_id = user_id
        super(UserRoleMappingsRealm, self).__init__(*args, **kwargs)

    def available_realm_role(self):
        return self._client.get(
            url=self._client.get_full_url(
                self.get_path(
                    'available', realm=self._realm_name, id=self._user_id
                )
            )
        )

    def add_realm_role(self, roles):
        """
        :param roles: _rolerepresentation keycloak api
        """
        return self._client.post(
            url=self._client.get_full_url(
                self.get_path(
                    'single', realm=self._realm_name, id=self._user_id
                )
            ),
            data=json.dumps(roles, sort_keys=True)
        )
