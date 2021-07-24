from CanvasClient import CanvasClient


class CanvasAnayltics(CanvasClient):

    def __init__(self):

        self.account_id = None
        self.term_id = None

    def generate_queries(self):

        body = {}

        return None


    def clear_queries(self):

        self.account_id = None
        self.term_id = None