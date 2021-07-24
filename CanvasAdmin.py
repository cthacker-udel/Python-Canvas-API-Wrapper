from CanvasClient import CanvasClient

class CanvasAdmin(CanvasClient):

    def __init__(self):

        self.user_id = None
        self.role = None
        self.role_id = None
        self.account_id = None
        self.send_confirmation = None
        self.admin_id = None
        self.user_ids = []


    def generate_queries(self):

        body = {}

        if self.user_id != None:
            body['user_id'] = self.user_id
        if self.role != None:
            body['role'] = self.role
        if self.role_id != None:
            body['role_id'] = self.role_id
        if self.send_confirmation != None:
            body['send_confirmation'] = self.send_confirmation
        if len(self.user_ids) > 0:
            body['user_id[]'] = self.user_ids
        return body

    def clear_queries(self):
        self.user_id = None
        self.role = None
        self.role_id = None
        self.send_confirmation = None
        self.account_id = None
        self.user_ids = []
        self.admin_id = None
