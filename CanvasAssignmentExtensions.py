from CanvasClient import CanvasClient

class CanvasAssignmentExtensions(CanvasClient):

    def __init__(self):
        self.user_id = None
        self.extra_attempts = None
        self.course_id = None
        self.assignment_id = None

    def generate_queries(self):

        body = {}

        if self.user_id != None:
            body['assignment_extensions[][user_id]'] = self.user_id
        if self.extra_attempts != None:
            body['assignment_extensions[][extra_attempts]'] = self.extra_attempts
        return body

    def clear_queries(self):
        self.user_id = None
        self.extra_attempts = None
