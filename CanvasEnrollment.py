from CanvasClient import CanvasClient

class CanvasEnrollment(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.section_id = None
        self.user_id = None
        self.enrollment_id = None
        self.account_id = None

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
        self.id = None

        self.enrollment_start_at = None
        self.enrollment_end_at = None
        self.enrollment_user_id = None
        self.enrollment_type = None
        self.enrollment_role = None
        self.enrollment_role_id = None
        self.enrollment_state = None
        self.enrollment_course_section_id = None
        self.enrollment_limit_privileges_to_section = None
        self.enrollment_notify = None
        self.enrollment_code = None
        self.enrollment_self_enrolled = None
        self.enrollment_associated_user_id = None

    def generate_queries(self):

        body = {}

        if self.id is not None:
            body['id'] = self.id
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
        if self.enrollment_start_at is not None:
            body['enrollment[start_at]'] = self.enrollment_start_at
        if self.enrollment_end_at is not None:
            body['enrollment[end_at]'] = self.enrollment_end_at
        if self.enrollment_user_id is not None:
            body['enrollment[user_id]'] = self.enrollment_user_id
        if self.enrollment_type is not None:
            body['enrollment[type]'] = self.enrollment_type
        if self.enrollment_role is not None:
            body['enrollment[role]'] = self.enrollment_role
        if self.enrollment_role_id is not None:
            body['enrollment[role_id]'] = self.enrollment_role_id
        if self.enrollment_state is not None:
            body['enrollment[enrollment_state]'] = self.enrollment_state
        if self.enrollment_course_section_id is not None:
            body['enrollment[course_section_id]'] = self.enrollment_course_section_id
        if self.enrollment_limit_privileges_to_section is not None:
            body['enrollment[limit_privileges_to_course_section]'] = self.enrollment_limit_privileges_to_section
        if self.enrollment_notify is not None:
            body['enrollment[notify]'] = self.enrollment_notify
        if self.enrollment_code is not None:
            body['enrollment[self_enrollment_code]'] = self.enrollment_code
        if self.enrollment_self_enrolled is not None:
            body['enrollment[self_enrolled]'] = self.enrollment_self_enrolled
        if self.enrollment_associated_user_id is not None:
            body['enrollment[associated_user_id]']= self.enrollment_associated_user_id
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
        self.id = None
        self.account_id = None