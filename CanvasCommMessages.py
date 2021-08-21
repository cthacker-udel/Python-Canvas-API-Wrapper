from CanvasClient import CanvasClient

class CanvasCommMessages(CanvasClient):

    def __init__(self):

        self.user_id = None
        self.start_time = None
        self.end_time = None


    def generate_queries(self):

        body = {}

        if self.user_id is not None:
            body['user_id'] = self.user_id
        if self.start_time is not None:
            body['start_time'] = self.start_time
        if self.end_time is not None:
            body['end_time'] = self.end_time
        return body

    def clear_queries(self):
        self.user_id = None
        self.start_time = None
        self.end_time = None