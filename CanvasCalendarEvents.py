from CanvasClient import CanvasClient

class CanvasCalendarEvents(CanvasClient):

    def __init__(self):

        self.user_id = None
        self.calendar_event_id = None
        self.participant_id = None
        self.course_id = None

        self.comments = None
        self.cancel_existing = None

        self.type = None
        self.start_date = None
        self.end_date = None
        self.undated = None
        self.all_events = None
        self.context_codes = None
        self.excludes = None
        self.important_dates = None

        self.calendar_context_code = None
        self.calendar_title = None
        self.calendar_description = None
        self.calendar_start_at = None
        self.calendar_end_at = None
        self.calendar_location_name = None
        self.calendar_location_address = None
        self.calendar_time_zone_edited = None
        self.calendar_all_day = None
        self.calendar_child_event_data_start_at = None
        self.calendar_child_event_data_end_at = None
        self.calendar_child_event_context_code = None
        self.calendar_duplicate_count = None
        self.calendar_duplicate_frequency = None
        self.calendar_duplicate_interval = None
        self.calendar_duplicate_append_iterator = None
        self.cancel_reason = None

    def generate_queries(self):

        body = {}

        if self.cancel_reason is not None:
            body['cancel_reason'] = self.cancel_reason
        if self.comments is not None:
            body['comments'] = self.comments
        if self.cancel_existing is not None:
            body['cancel_existing'] = self.cancel_existing
        if self.calendar_context_code is not None:
            body['calendar_event[context_code]'] = self.calendar_context_code
        if self.calendar_title is not None:
            body['calendar_event[title]'] = self.calendar_title
        if self.calendar_description is not None:
            body['calendar_event[description]'] = self.calendar_description
        if self.calendar_start_at is not None:
            body['calendar_event[start_at]'] = self.calendar_start_at
        if self.calendar_end_at is not None:
            body['calendar_event[end_at]'] = self.calendar_end_at
        if self.calendar_location_name is not None:
            body['calendar_event[location_name]'] = self.calendar_location_name
        if self.calendar_location_address is not None:
            body['calendar_event[location_address]'] = self.calendar_location_address
        if self.calendar_time_zone_edited is not None:
            body['calendar_event[time_zone_edited]'] = self.calendar_time_zone_edited
        if self.calendar_all_day is not None:
            body['calendar_event[all_day]'] = self.calendar_all_day
        if self.calendar_child_event_data_start_at is not None:
            body['calendar_event[child_event_data][X][start_at]'] = self.calendar_child_event_data_start_at
        if self.calendar_child_event_data_end_at is not None:
            body['calendar_event[child_event_data][X][end_at]'] = self.calendar_child_event_data_end_at
        if self.calendar_child_event_context_code is not None:
            body['calendar_event[child_event_data][X][context_code]'] = self.calendar_child_event_context_code
        if self.calendar_duplicate_count is not None:
            body['calendar_event[duplicate][count]'] = self.calendar_duplicate_count
        if self.calendar_duplicate_frequency is not None:
            body['calendar_event[duplicate][frequency]'] = self.calendar_duplicate_frequency
        if self.calendar_duplicate_interval is not None:
            body['calendar_event[duplicate][interval]'] = self.calendar_duplicate_interval
        if self.calendar_duplicate_append_iterator is not None:
            body['calendar_event[duplicate][append_iterator]'] = self.calendar_duplicate_append_iterator
        if self.type is not None:
            body['type'] = self.type
        if self.start_date is not None:
            body['start_date'] = self.start_date
        if self.end_date is not None:
            body['end_date'] = self.end_date
        if self.undated is not None:
            body['undated'] = self.undated
        if self.all_events is not None:
            body['all_events'] = self.all_events
        if self.context_codes is not None:
            body['context_codes[]'] = self.context_codes
        if self.excludes is not None:
            body['excludes[]'] = self.excludes
        if self.important_dates is not None:
            body['important_dates'] = self.important_dates
        return body

    def clear_queries(self):
        self.type = None
        self.start_date = None
        self.end_date = None
        self.undated = None
        self.all_events = None
        self.context_codes = None
        self.excludes = None
        self.important_dates = None
        self.calendar_context_code = None
        self.calendar_title = None
        self.calendar_description = None
        self.calendar_start_at = None
        self.calendar_end_at = None
        self.calendar_location_name = None
        self.calendar_location_address = None
        self.calendar_time_zone_edited = None
        self.calendar_all_day = None
        self.calendar_child_event_data_start_at = None
        self.calendar_child_event_data_end_at = None
        self.calendar_child_event_context_code = None
        self.calendar_duplicate_count = None
        self.calendar_duplicate_frequency = None
        self.calendar_duplicate_interval = None
        self.calendar_duplicate_append_iterator = None
        self.comments = None
        self.cancel_existing = None