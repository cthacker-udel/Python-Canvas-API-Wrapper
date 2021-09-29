from CanvasClient import CanvasClient

class CanvasFeatureFlags(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.account_id = None
        self.user_id = None
        self.feature_id = None

        self.state = None

    def generate_queries(self):

        body = {}

        if self.state is not None:
            body['state'] = self.state
        return body

    def clear_queries(self):
        self.course_id = None
        self.account_id = None
        self.user_id = None
        self.feature_id = None

        self.state = None