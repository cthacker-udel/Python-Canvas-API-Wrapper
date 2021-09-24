from CanvasClient import CanvasClient

class CanvasExternalTools(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.account_id = None
        self.group_id = None
        self.search_term = None
        self.selectable = None
        self.include_parents = None

        self.id = None
        self.url = None
        self.assignment_id = None
        self.module_item_id = None
        self.launch_type = None


    def generate_queries(self):

        body = {}

        if self.id is not None:
            body['id'] = self.id
        if self.url is not None:
            body['url'] = self.url
        if self.assignment_id is not None:
            body['assignment_id'] = self.assignment_id
        if self.module_item_id is not None:
            body['module_item_id'] = self.module_item_id
        if self.launch_type is not None:
            body['launch_type'] = self.launch_type
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