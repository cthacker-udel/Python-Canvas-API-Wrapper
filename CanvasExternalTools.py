from CanvasClient import CanvasClient

class CanvasExternalTools(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.account_id = None
        self.group_id = None
        self.search_term = None
        self.selectable = None
        self.include_parents = None


    def generate_queries(self):

        body = {}

        if self.search_term is not None:
            body['search_term'] = self.search_term
        if self.selectable is not None:
            body['selectable'] = self.selectable
        if self.include_parents is not None:
            body['include_parents'] = self.include_parents
        return body

    def clear_queries(self):

        self.search_term = None
        self.selectable = None
        self.include_parents = None