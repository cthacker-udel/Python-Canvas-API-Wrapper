from CanvasClient import CanvasClient


class CanvasExternalFeed(CanvasClient):

    def __init__(self):

        self.url = None
        self.header_match = None
        self.verbosity = None
        self.course_id = None
        self.group_id = None

    def generate_queries(self):

        body = {}

        if self.url != None:
            body['url'] = self.url
        if self.header_match != None:
            body['header_match'] = self.header_match
        if self.verbosity != None:
            body['verbosity'] = self.verbosity
        return body

    def clear_queries(self):

        self.url = None
        self.header_match = None
        self.verbosity = None