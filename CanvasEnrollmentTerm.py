from CanvasClient import CanvasClient

class CanvasEnrollmentTerms(CanvasClient):

    def __init__(self):

        self.account_id = None
        self.term_id = None

        self.enrollment_term_name = None
        self.enrollment_term_start_at = None
        self.enrollment_term_end_at = None
        self.enrollmen_term_overrides_start_at = None
        self.enrollment_term_overrides_end_at = None
        self.enrollment_sis_term_id = None

        self.workflow_state = None
        self.include = None

    def generat_queries(self):

        body = {}

        if self.enrollment_term_name is not None:
            body['enrollment_term[name]'] = self.enrollment_term_name
        if self.enrollment_term_start_at is not None:
            body['enrollment_term[start_at]'] = self.enrollment_term_start_at
        if self.enrollment_term_end_at is not None:
            body['enrollment_term[end_at]'] = self.enrollment_term_end_at
        if self.enrollmen_term_overrides_start_at is not None:
            body['enrollment_term[overrides][enrollment_type][start_at]'] = self.enrollmen_term_overrides_start_at
        if self.enrollment_term_overrides_end_at is not None:
            body['enrollment_term[overrides][enrollment_type][end_at]'] = self.enrollment_term_overrides_end_at
        if self.enrollment_sis_term_id is not None:
            body['enrollment_term[sis_term_id]'] = self.enrollment_sis_term_id
        if self.workflow_state is not None:
            body['workflow_state[]'] = self.workflow_state
        if self.include is not None:
            body['include[]'] = self.include
        return body