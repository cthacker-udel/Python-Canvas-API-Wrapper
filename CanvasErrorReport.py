from CanvasClient import CanvasClient

class CanvasErrorReport(CanvasClient):

    def __init__(self):

        self.error_subject = None
        self.error_url = None
        self.error_email = None
        self.error_comments = None
        self.error_http_env = None


    def generate_queries(self):

        body = {}

        if self.error_subject is not None:
            body['error[subject]'] = self.error_subject
        if self.error_url is not None:
            body['error[url]'] = self.error_url
        if self.error_email is not None:
            body['error[email]'] = self.error_email
        if self.error_comments is not None:
            body['error[comments]'] = self.error_comments
        if self.error_http_env is not None:
            body['error[http_env]'] = self.error_http_env
        return body


    def clear_queries(self):

        self.error_subject = None
        self.error_url = None
        self.error_email = None
        self.error_comments = None
        self.error_http_env = None