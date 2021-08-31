from CanvasClient import CanvasClient


class CanvasCourseAuditLog(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.start_time = None
        self.end_time = None
        self.account_id = None

    def generate_queries(self):

        body = {}

        if self.start_time is not None:
            body['start_time'] = self.start_time
        if self.end_time is not None:
            body['end_time'] = self.end_time
        return body


    def clear_queries(self):

        self.course_id = None
        self.start_time = None
        self.end_time = None
        self.account_id = None