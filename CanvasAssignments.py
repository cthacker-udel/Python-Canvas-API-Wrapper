from CanvasClient import CanvasClient

class CanvasAssignments(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.assignment_id = None

        self.include = None
        self.search_term = None
        self.override_assignment_dates = None
        self.needs_grading_count_by_section = None
        self.bucket = None
        self.assingment_ids = None
        self.order_by = None
        self.post_to_sis = None
        self.result_type = None
        self.all_dates = None

        self.assignment_name = None
        self.assignment_position = None
        self.assignment_submission_types = None
        self.assignment_allowed_extensions = None
        self.turnitin_enabled = None
        self.vericite_enabled = None
        self.turnitin_settings = None
        self.integration_data = None
        self.integration_id = None
        self.peer_reviews = None
        self.automatic_peer_reviews = None
        self.notify_of_update = None
        self.group_category_id = None
        self.grade_group_students_individually = None
        self.external_tool_tag_attributes = None
        self.points_possible = None
        self.grading_type = None
        self.due_at = None
        self.lock_at = None
        self.unlock_at = None
        self.description = None
        self.assignment_group_id = None
        self.assignment_overrides = None
        self.only_visible_to_overrides = None
        self.published = None
        self.grading_standard_id = None
        self.omit_from_final_grade = None
        self.quiz_lti = None
        self.moderated_grading = None
        self.grader_count = None
        self.final_grader_id = None
        self.grader_comments_visible_to_graders = None
        self.graders_anonymous_to_graders = None
        self.graders_names_visible_to_final_grader = None
        self.anonymous_grading = None
        self.allowed_attempts = None
        self.annotatable_attachment_id = None

    def clear_queries(self):

        self.include = None
        self.search_term = None
        self.override_assignment_dates = None
        self.needs_grading_count_by_section = None
        self.bucket = None
        self.assingment_ids = None
        self.order_by = None
        self.post_to_sis = None
        self.result_type = None
        self.all_dates = None

        self.assignment_name = None
        self.assignment_position = None
        self.assignment_submission_types = None
        self.assignment_allowed_extensions = None
        self.turnitin_enabled = None
        self.vericite_enabled = None
        self.turnitin_settings = None
        self.integration_data = None
        self.integration_id = None
        self.peer_reviews = None
        self.automatic_peer_reviews = None
        self.notify_of_update = None
        self.group_category_id = None
        self.grade_group_students_individually = None
        self.external_tool_tag_attributes = None
        self.points_possible = None
        self.grading_type = None
        self.due_at = None
        self.lock_at = None
        self.unlock_at = None
        self.description = None
        self.assignment_group_id = None
        self.assignment_overrides = None
        self.only_visible_to_overrides = None
        self.published = None
        self.grading_standard_id = None
        self.omit_from_final_grade = None
        self.quiz_lti = None
        self.moderated_grading = None
        self.grader_count = None
        self.final_grader_id = None
        self.grader_comments_visible_to_graders = None
        self.graders_anonymous_to_graders = None
        self.graders_names_visible_to_final_grader = None
        self.anonymous_grading = None
        self.allowed_attempts = None
        self.annotatable_attachment_id = None
