from CanvasClient import CanvasClient

class CanvasBookmark(CanvasClient):

    def __init__(self):

        self.bookmark_id = None
        self.name = None
        self.url = None
        self.position = None
        self.data = None


    def generate_queries(self):

        body = {}

        if self.name is not None:
            body['name'] = self.name
        if self.url is not None:
            body['url'] = self.url
        if self.position is not None:
            body['position'] = self.position
        if self.data is not None:
            body['data'] = self.data
        return body

    def clear_queries(self):

        self.name = None
        self.url = None
        self.position = None
        self.data = None