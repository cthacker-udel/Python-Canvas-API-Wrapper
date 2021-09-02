from CanvasClient import CanvasClient

class CanvasCourses(CanvasClient):

    def __init__(self):

        self.user_id = None
        self.course_id = None
        self.account_id = None

        self.enrollment_type = None
        self.enrollment_role = None
        self.enrollment_role_id = None
        self.enrollment_state = None
        self.exclude_blueprint_courses = None
        self.include = None
        self.state = None

        self.course_name = None
        self.course_code = None
        self.course_start_at = None
        self.course_end_at = None
        self.course_license = None
        self.course_is_public = None
        self.course_is_public_to_auth_users = None
        self.course_public_syllabus = None
        self.course_public_syllabus_to_auth = None
        self.course_public_description = None
        self.course_allow_student_wiki_edits = None
        self.course_allow_wiki_comments = None
        self.course_allow_student_forum_attachments = None
        self.open_enrollment = None
        self.self_enrollment = None
        self.restrict_enrollments_to_course_dates = None
        self.term_id = None
        self.sis_course_id = None
        self.integration_id = None
        self.hide_final_grades = None
        self.apply_assignment_group_weight = None
        self.course_time_zone = None
        self.offer = None
        self.enroll_me = None
        self.course_default_view = None
        self.syllabus_body = None
        self.grading_standard_id = None
        self.grade_passback_setting = None
        self.course_format = None
        self.enable_sis_reactivation = None


    def generate_queries(self):

        body = {}

        if self.enrollment_type is not None:
            body['enrollment_type'] = self.enrollment_type
        if self.enrollment_role is not None:
            body['enrollment_role'] = self.enrollment_role
        if self.enrollment_role_id is not None:
            body['enrollment_role_id'] = self.enrollment_role_id
        if self.enrollment_state is not None:
            body['enrollment_state'] = self.enrollment_state
        if self.exclude_blueprint_courses is not None:
            body['exclude_blueprint_courses'] = self.exclude_blueprint_courses
        if self.include is not None:
            body['include[]'] = self.include
        if self.state is not None:
            body['state'] = self.state
        return body

    def clear_queries(self):

        self.enrollment_type = None
        self.enrollment_role = None
        self.enrollment_state = None
        self.enrollment_role_id = None
        self.state = None
        self.exclude_blueprint_courses = None
        self.include = None
        self.state = None
        self.user_id = None
        self.course_id = None