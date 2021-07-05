
import import_declare_test

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    SingleModel,
)
from splunktaucclib.rest_handler import admin_external, util
from splunktaucclib.rest_handler.admin_external import AdminExternalHandler
import logging

util.remove_http_proxy_env_vars()


fields = [
    field.RestField(
        'jira_env',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.AllOf(
            validator.String(
                max_len=50, 
                min_len=1, 
            ), 
            validator.Pattern(
                regex=r"""^[a-zA-Z]\w*$""", 
            )
        )
    ), 
    field.RestField(
        'jira_url',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'jira_default_account',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'configuration_help_link',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'account_radio',
        required=True,
        encrypted=False,
        default='yes',
        validator=None
    ), 
    field.RestField(
        'jira_ssl_certificate_path',
        required=False,
        encrypted=False,
        default=None,
        validator=validator.String(
            max_len=4096, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'username',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'password',
        required=False,
        encrypted=True,
        default=None,
        validator=None
    ), 
    field.RestField(
        'client_id',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'client_secret',
        required=False,
        encrypted=True,
        default=None,
        validator=None
    ), 
    field.RestField(
        'redirect_url',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'access_token',
        required=False,
        encrypted=True,
        default=None,
        validator=None
    ), 
    field.RestField(
        'refresh_token',
        required=False,
        encrypted=True,
        default=None,
        validator=None
    ), 
    field.RestField(
        'instance_url',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'auth_type',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    )
]
model = RestModel(fields, name=None)


endpoint = SingleModel(
    'ta_service_desk_simple_addon_account',
    model,
    config_name='account'
)


if __name__ == '__main__':
    logging.getLogger().addHandler(logging.NullHandler())
    admin_external.handle(
        endpoint,
        handler=AdminExternalHandler,
    )
