from CanvasClient import CanvasClient



class CanvasAccountDomainLookup(CanvasClient):

    def __init__(self):

        self.name = None
        self.domain = None
        self.latitude = None
        self.longitude = None

    def generate_queries(self):

        body = {}

        if self.name != None:
            body['name'] = self.name
        if self.domain != None:
            body['domain'] = self.domain
        if self.latitude != None:
            body['latitude'] = self.latitude
        if self.longitude != None:
            body['longitude'] = self.longitude
        return body

    def clear_queries(self):
        self.name = None
        self.domain = None
        self.latitude = None
        self.longitude = None