from CanvasClient import CanvasClient

class CanvasAppointmentGroup(CanvasClient):

    def __init__(self):

        self.appointment_group_id = None
        self.scope = None
        self.context_codes = None
        self.include_past_appointments = None
        self.include = None


    def generate_queries(self):

        body = {}

        if self.scope != None:
            body['scope'] = self.scope
        if self.context_codes != None:
            body['context_codes[]'] = self.context_codes
        if self.include_past_appointments != None:
            body['include_past_appointments'] = self.include_past_appointments
        if self.include != None:
            body['include[]'] = self.include
        return body


    def clear_queries(self):

        self.scope = None
        self.context_codes = None
        self.include_past_appointments = None
        self.include = None