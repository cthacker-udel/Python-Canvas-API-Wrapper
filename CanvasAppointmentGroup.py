from CanvasClient import CanvasClient

class CanvasAppointmentGroup(CanvasClient):

    def __init__(self):

        self.appointment_group_id = None
        self.scope = None
        self.context_codes = None
        self.include_past_appointments = None
        self.include = None

        self.appt_context_codes = None
        self.appt_sub_context_codes = None
        self.appt_title = None
        self.appt_description = None
        self.appt_location_name = None
        self.appt_location_address = None
        self.appt_publish = None
        self.appt_participants_per_appointment = None
        self.appt_min_appointments_per_participant = None
        self.appt_max_appointments_per_participant = None
        self.appt_new_appointments = None
        self.appt_participant_visibility = None

        self.cancel_reason = None

        self.registration_status = None


    def generate_queries(self):

        body = {}
        if self.registration_status != None:
            body['registration_status'] = self.registration_status
        if self.cancel_reason != None:
            body['cancel_reason'] = self.cancel_reason
        if self.appt_context_codes != None:
            body['appointment_group[context_codes][]'] = self.appt_context_codes
        if self.appt_sub_context_codes != None:
            body['appointment_group[sub_context_codes][]'] = self.appt_sub_context_codes
        if self.appt_title != None:
            body['appointment_group[title]'] = self.appt_title
        if self.appt_description != None:
            body['appointment_group[description]'] = self.appt_description
        if self.appt_location_name != None:
            body['appointment_group[location_name]'] = self.appt_location_name
        if self.appt_location_address != None:
            body['appointment_group[location_address]'] = self.appt_location_address
        if self.appt_publish != None:
            body['appointment_group[publish]'] = self.appt_publish
        if self.appt_participants_per_appointment != None:
            body['appointment_group[participants_per_appointment]'] = self.appt_participants_per_appointment
        if self.appt_min_appointments_per_participant != None:
            body['appointment_group[min_appointments_per_participant]'] = self.appt_min_appointments_per_participant
        if self.appt_max_appointments_per_participant != None:
            body['appointment_group[max_appointments_per_participant]'] = self.appt_max_appointments_per_participant
        if self.appt_new_appointments != None:
            body['appointment_group[new_appointments][X][]'] = self.appt_new_appointments
        if self.appt_participant_visibility != None:
            body['appointment_group[participant_visibility]'] = self.appt_participant_visibility
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
        self.appt_context_codes = None
        self.appt_sub_context_codes = None
        self.appt_title = None
        self.appt_description = None
        self.appt_location_address = None
        self.appt_location_name = None
        self.appt_publish = None
        self.appt_participants_per_appointment = None
        self.appt_min_appointments_per_participant = None
        self.appt_max_appointments_per_participant = None
        self.appt_new_appointments = None
        self.appt_participant_visibility = None
        self.cancel_reason = None
        self.registration_status = None