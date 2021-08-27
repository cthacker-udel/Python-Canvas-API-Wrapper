from CanvasClient import CanvasClient

class CanvasContentSecurityPolicySettings(CanvasClient):

    def __init__(self):

        self.status = None
        self.settings_locked = None
        self.domain = None
        self.domains = None

    def generate_queries(self):

        body = {}

        if self.status != None:
            body['status'] = self.status
        if self.settings_locked != None:
            body['settings_locked'] = self.settings_locked
        if self.domain != None:
            body['domain'] = self.domain
        if self.domains != None:
            body['domains'] = self.domains
        return body

    def clear_queries(self):

        self.status = None
        self.settings_locked = None
        self.domain = None
        self.domains = None