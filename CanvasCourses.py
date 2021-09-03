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

        self.search_term = None
        self.sort = None
        self.enrollment_type_student_list = None

        self.html = None

    def generate_queries(self):

        body = {}

        if self.html is not None:
            body['html'] = self.html
        if self.enrollment_type_student_list is not None:
            body['enrollment_type[]'] = self.enrollment_type_student_list
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
        if self.course_name is not None:
            body['course[name]'] = self.course_name
        if self.course_code is not None:
            body['course[course_code]'] = self.course_code
        if self.course_start_at is not None:
            body['course[start_at]'] = self.course_start_at
        if self.course_end_at is not None:
            body['course[end_at]'] = self.course_end_at
        if self.course_license is not None:
            body['course[license]'] = self.course_license
        if self.course_is_public is not None:
            body['course[is_public]'] = self.course_is_public
        if self.course_is_public_to_auth_users is not None:
            body['course[is_public_to_auth_users]'] = self.course_is_public_to_auth_users
        if self.course_public_syllabus is not None:
            body['course[public_syllabus]'] = self.course_public_syllabus
        if self.course_public_syllabus_to_auth is not None:
            body['course[public_syllabus_to_auth]'] = self.course_public_syllabus_to_auth
        if self.course_public_description is not None:
            body['course[public_description]'] = self.course_public_description
        if self.course_allow_student_wiki_edits is not None:
            body['course[allow_student_wiki_edits]'] = self.course_allow_student_wiki_edits
        if self.course_allow_wiki_comments is not None:
            body['course[allow_wiki_comments]'] = self.course_allow_wiki_comments
        if self.course_allow_student_forum_attachments is not None:
            body['course[allow_student_forum_attachments]'] = self.course_allow_student_forum_attachments
        if self.open_enrollment is not None:
            body['course[open_enrollment]'] = self.open_enrollment
        if self.self_enrollment is not None:
            body['course[self_enrollment]'] = self.self_enrollment
        if self.restrict_enrollments_to_course_dates is not None:
            body['course[restrict_enrollments_to_course_dates]'] = self.restrict_enrollments_to_course_dates
        if self.term_id is not None:
            body['course[term_id]'] = self.term_id
        if self.sis_course_id is not None:
            body['course[sis_course_id]'] = self.sis_course_id
        if self.integration_id is not None:
            body['course[integration_id]'] = self.integration_id
        if self.hide_final_grades is not None:
            body['course[hide_final_grades]'] = self.hide_final_grades
        if self.apply_assignment_group_weight is not None:
            body['course[apply_assignment_group_weights]'] = self.apply_assignment_group_weight
        if self.course_time_zone is not None:
            body['course[time_zone]'] = self.course_time_zone
        if self.offer is not None:
            body['offer'] = self.offer
        if self.enroll_me is not None:
            body['enroll_me'] = self.enroll_me
        if self.course_default_view is not None:
            body['course[default_view]'] = self.course_default_view
        if self.syllabus_body is not None:
            body['course[syllabus_body]'] = self.syllabus_body
        if self.grading_standard_id is not None:
            body['course[grading_standard_id]'] = self.grading_standard_id
        if self.grade_passback_setting is not None:
            body['course[grade_passback_setting]'] = self.grade_passback_setting
        if self.course_format is not None:
            body['course[course_format]'] = self.course_format
        if self.enable_sis_reactivation is not None:
            body['enable_sis_reactivation'] = self.enable_sis_reactivation
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
        self.enrollment_type_student_list = None

        self.html = None