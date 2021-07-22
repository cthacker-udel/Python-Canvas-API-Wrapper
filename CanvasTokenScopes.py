from CanvasClient import CanvasClient

class CanvasTokenScopes(CanvasClient):

    def __init__(self):
        self.group_by = None
        self.account_id = None


    def generate_queries(self):

        body = {}

        if self.group_by != None:
            body['group_by'] = self.group_by
        return body

    def clear_queries(self):
        self.group_by = None