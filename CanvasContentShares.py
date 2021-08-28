from CanvasClient import CanvasClient

class CanvasContentShares(CanvasClient):

    def __init__(self):

        self.user_id = None
        self.account_id = None
        self.content_share_id = None


        self.receiver_ids = None
        self.content_type = None
        self.content_id = None
        self.read_state = None

    def generate_queries(self):

        body = {}

        if self.receiver_ids is not None:
            body['receiver_ids'] = self.receiver_ids
        if self.content_id is not None:
            body['content_id'] = self.content_id
        if self.content_type is not None:
            body['content_type'] = self.content_type
        if self.read_state is not None:
            body['read_state'] = self.read_state
        return body


