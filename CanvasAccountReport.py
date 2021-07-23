from CanvasClient import CanvasClient


class CanvasAccountReport(CanvasClient):

    def __init__(self):
        self.account_id = None
        self.report_id = None
        self.parameters = None
        self.parameters_course_id = None
        self.parameters_users = None

    def generate_queries(self):

        body = {}

        if self.parameters != None:
            body['parameters'] = self.parameters
        if self.parameters_course_id != None:
            body['parameters[course_id]'] = self.parameters_course_id
        if self.parameters_users != None:
            body['parameters[users]'] = self.parameters_users
        return body

    def clear_queries(self):

        self.account_id = None
        self.report_id = None
        self.parameters = None
        self.parameters_course_id = None
        self.parameters_users = None