from CanvasClient import CanvasClient

class CanvasCollaboration(CanvasClient):

    def __init__(self):

        self.include = None
        self.collaboration_id = None
        self.course_id = None
        self.group_id = None


    def generate_queries(self):

        body = {}

        if self.include is not None:
            body['include[]'] = self.include

        return body

    def clear_queries(self):

        self.include = None
        self.collaboration_id = None
        self.course_id = None
        self.group_id = None