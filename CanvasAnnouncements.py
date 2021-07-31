from CanvasClient import client


class CanvasAnnouncement(CanvasClient):

    def __init__(self):

        self.context_codes = None
        self.start_date = None
        self.end_date = None
        self.active_only = None
        self.latest_only = None
        self.include = None


    def generate_queries(self):

        body = {}

        if self.context_codes != None:
            body['context_codes[]'] = self.context_codes
        if self.start_date != None:
            body['start_date'] = self.start_date
        if self.end_date != None:
            body['end_date'] = self.end_date
        if self.active_only != None:
            body['active_only'] = self.active_only
        if self.latest_only != None:
            body['latest_only'] = self.latest_only
        if self.include != None:
            body['include'] = self.include
        return body

    def clear_queries(self):
        self.context_codes = None
        self.start_date = None
        self.end_date = None
        self.active_only = None
        self.latest_only = None
        self.include = None