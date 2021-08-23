from CanvasClient import CanvasClient

class CanvasConferences(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.group_id = None

        self.state = None

    def generate_queries(self):

        body = {}

        if self.state is not None:
            body['state'] = self.state
        return body

    def clear_queries(self):

        self.state = None
        self.course_id = None
        self.group_id = None