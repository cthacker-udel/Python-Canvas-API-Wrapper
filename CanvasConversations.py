from CanvasClient import CanvasClient

class CanvasConversations(CanvasClient):


    def __init__(self):

        self.scope = None
        self.filter = None
        self.filter_mode = None
        self.interleave_submissions = None
        self.include_all_conversation_ids = None
        self.include = None


    def generate_queries(self):

        body = {}

        if self.scope is not None:
            body['scope'] = self.scope
        if self.filter is not None:
            body['filter[]'] = self.filter
        if self.filter_mode is not None:
            body['filter_mode'] = self.filter_mode
        if self.interleave_submissions is not None:
            body['interleave_submissions'] = self.interleave_submissions
        if self.include_all_conversation_ids is not None:
            body['include_all_conversation_ids'] = self.include_all_conversation_ids
        if self.include is not None:
            body['include[]'] = self.include
        return body

    def clear_queries(self):

        self.scope = None
        self.filter = None
        self.filter_mode = None
        self.interleave_submissions = None
        self.include_all_conversation_ids = None
        self.include = None