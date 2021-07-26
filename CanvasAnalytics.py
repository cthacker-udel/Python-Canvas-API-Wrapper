from CanvasClient import CanvasClient


class CanvasAnayltics(CanvasClient):

    def __init__(self):

        self.account_id = None
        self.term_id = None
        self.course_id = None
        self.user_id = None

        self.sort_column = None
        self.student_id = None

    def generate_queries(self):

        body = {}

        if self.sort_column != None:
            body['sort_column'] = self.sort_column
        if self.student_id != None:
            body['student_id'] = self.student_id

        return body


    def clear_queries(self):

        self.account_id = None
        self.term_id = None
        self.course_id = None
        self.sort_column = None
        self.student_id = None