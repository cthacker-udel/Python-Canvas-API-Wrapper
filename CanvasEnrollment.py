from CanvasClient import CanvasClient

class CanvasEnrollment(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.section_id = None
        self.user_id = None
        self.enrollment_id = None

        self.type = None
        self.role = None
        self.state = None
        self.include = None
        self.grading_period_id = None
        self.enrollment_term_id = None
        self.sis_account_id = None
        self.sis_course_id = None
        self.sis_section_id = None
        self.sis_user_id = None
        self.created_for_sis_id = None

    def generate_queries(self):

        body = {}

        if self.type is not None:
            body['type[]'] = self.type
        if self.role is not None:
            body['role[]'] = self.role
        if self.state is not None:
            body['state[]'] = self.state
        if self.include is not None:
            body['include[]'] = self.include
        if self.user_id is not None:
            body['user_id'] = self.user_id
        if self.grading_period_id is not None:
            body['grading_period_id'] = self.grading_period_id
        if self.enrollment_term_id is not None:
            body['enrollment_term_id'] = self.enrollment_term_id
        if self.sis_account_id is not None:
            body['sis_account_id[]'] = self.sis_account_id
        if self.sis_course_id is not None:
            body['sis_course_id[]'] = self.sis_course_id
        if self.sis_section_id is not None:
            body['sis_section_id[]'] = self.sis_section_id
        if self.sis_user_id is not None:
            body['sis_user_id[]'] = self.sis_user_id
        if self.created_for_sis_id is not None:
            body['created_for_sis_id[]'] = self.created_for_sis_id
        return body

    def clear_queries(self):

        self.course_id = None
        self.section_id = None
        self.user_id = None
        self.enrollment_id = None

        self.type = None
        self.role = None
        self.state = None
        self.include = None
        self.grading_period_id = None
        self.enrollment_term_id = None
        self.sis_account_id = None
        self.sis_course_id = None
        self.sis_section_id = None
        self.sis_user_id = None
        self.created_for_sis_id = None