from CanvasClient import CanvasClient

class CanvasCommunicationChannel(CanvasClient):

    def __init__(self):

        self.user_id = None
        self.communication_channel_address = None
        self.communication_channel_type = None
        self.communication_channel_token = None
        self.skip_confirmation = None

        self.communication_channel_id = None

    def generate_queries(self):

        body = {}

        if self.communication_channel_address is not None:
            body['communication_channel[address]'] = self.communication_channel_address
        if self.communication_channel_type is not None:
            body['communication_channel[type]'] = self.communication_channel_type
        if self.communication_channel_token is not None:
            body['communication_channel[token]'] = self.communication_channel_token
        if self.skip_confirmation is not None:
            body['skip_confirmation'] = self.skip_confirmation
        return body

    def clear_queries(self):

        self.communication_channel_token = None
        self.communication_channel_type = None
        self.communication_channel_id = None
        self.communication_channel_address = None
        self.skip_confirmation = None
        self.user_id = None