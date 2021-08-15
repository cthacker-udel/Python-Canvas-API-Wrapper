from CanvasClient import CanvasClient

class CanvasAuthProvider(CanvasClient):

    def __init__(self):

        self.account_id = None
        self.client_id = None
        self.login_attribute = None
        self.federated_attributes = None
        self.self_registration = None
        self.auth_base = None
        self.log_in_url = None
        self.log_out_url = None
        self.client_secret = None
        self.district_id = None
        self.app_id = None
        self.app_secret = None
        self.domain = None
        self.hosted_domain = None
        self.auth_host = None
        self.auth_port = None
        self.auth_over_tls = None
        self.auth_base = None
        self.auth_filter = None
        self.identifier_format = None
        self.auth_username = None
        self.auth_password = None
        self.application_id = None
        self.application_secret = None
        self.tenant = None
        self.authorize_url = None
        self.token_url = None
        self.scope = None
        self.end_session_endpoint = None
        self.userinfo_endpoint = None
        self.metadata = None
        self.metadata_uri = None
        self.idp_entity_id = None
        self.certificate_fingerprint = None
        self.requested_authn_context = None
        self.sig_alg = None
        self.consumer_key = None
        self.consumer_secret = None
        self.parent_registration = None

    def generate_queries(self):

        body = {}

        if self.client_id is not None:
            body['client_id'] = self.client_id
        if self.login_attribute is not None:
            body['login_attribute'] = self.login_attribute
        if self.federated_attributes is not None:
            body['federated_attributes']  = self.federated_attributes
        if self.self_registration is not None:
            body['self_registration'] = self.self_registration
        if self.auth_base is not None:
            body['auth_base'] = self.auth_base
        if self.log_in_url is not None:
            body['log_in_url'] = self.log_in_url
        if self.client_secret is not None:
            body['client_secret'] = self.client_secret
        if self.district_id is not None:
            body['district_id'] = self.district_id
        if self.app_id is not None:
            body['app_id'] = self.app_id
        if self.app_secret is not None:
            body['app_secret'] = self.app_secret
        if self.domain is not None:
            body['domain'] = self.domain
        if self.hosted_domain is not None:
            body['hosted_domain'] = self.hosted_domain
        if self.auth_host is not None:
            body['auth_host'] = self.auth_host
        if self.auth_port is not None:
            body['auth_port'] = self.auth_port
        if self.auth_over_tls is not None:
            body['auth_over_tls'] = self.auth_over_tls
        if self.auth_filter is not None:
            body['auth_filter'] = self.auth_filter
        if self.identifier_format is not None:
            body['identifier_format'] = self.identifier_format
        if self.auth_username is not None:
            body['auth_username'] = self.auth_username
        if self.auth_password is not None:
            body['auth_password'] = self.auth_password
        if self.application_id is not None:
            body['application_id'] = self.application_id
        if self.application_secret is not None:
            body['application_secret'] = self.application_secret
        if self.tenant is not None:
            body['tenant'] = self.tenant
        if self.authorize_url is not None:
            body['authorize_url'] = self.authorize_url
        if self.token_url is not None:
            body['token_url'] = self.token_url
        if self.scope is not None:
            body['scope'] = self.scope
        if self.end_session_endpoint is not None:
            body['end_session_endpoint'] = self.end_session_endpoint
        if self.userinfo_endpoint is not None:
            body['userinfo_endpoint'] = self.userinfo_endpoint
        if self.metadata is not None:
            body['metadata'] = self.metadata
        if self.metadata_uri is not None:
            body['metadata_uri'] = self.metadata_uri
        if self.idp_entity_id is not None:
            body['idp_entity_id'] = self.idp_entity_id
        if self.log_in_url is not None:
            body['log_in_url'] = self.log_in_url
        if self.log_out_url is not None:
            body['log_out_url'] = self.log_out_url
        if self.certificate_fingerprint is not None:
            body['certificate_fingerprint'] = self.certificate_fingerprint
        if self.requested_authn_context is not None:
            body['requested_authn_context'] = self.requested_authn_context
        if self.sig_alg is not None:
            body['sig_alg'] = self.sig_alg
        if self.consumer_secret is not None:
            body['consumer_secret'] = self.consumer_secret
        if self.consumer_key is not None:
            body['consumer_key'] = self.consumer_key
        if self.parent_registration is not None:
            body['parent_registration'] = self.parent_registration
        return body

    def clear_queries(self):
        self.account_id = None
        self.client_id = None
        self.login_attribute = None
        self.federated_attributes = None
        self.self_registration = None
        self.auth_base = None
        self.log_in_url = None
        self.client_secret = None
        self.district_id = None
        self.app_id = None
        self.app_secret = None
        self.domain = None
        self.hosted_domain = None
        self.auth_host = None
        self.auth_port = None
        self.auth_over_tls = None
        self.auth_base = None
        self.auth_filter = None
        self.identifier_format = None
        self.auth_username = None
        self.auth_password = None
        self.application_id = None
        self.application_secret = None
        self.tenant = None
        self.authorize_url = None
        self.token_url = None
        self.scope = None
        self.end_session_endpoint = None
        self.userinfo_endpoint = None
        self.metadata = None
        self.metadata_uri = None
        self.idp_entity_id = None
        self.certificate_fingerprint = None
        self.requested_authn_context = None
        self.sig_alg = None
        self.consumer_key = None
        self.consumer_secret = None
        self.parent_registration = None