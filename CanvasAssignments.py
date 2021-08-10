from CanvasClient import CanvasClient

class CanvasAssignments(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.assignment_id = None
        self.user_id = None

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

        self.override_id = None

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


    def generate_queries(self):

        body = {}

        if self.include != None:
            body['include[]'] = self.include
        if self.search_term != None:
            body['search_term'] = self.search_term
        if self.override_assignment_dates != None:
            body['override_assignment_dates'] = self.override_assignment_dates
        if self.needs_grading_count_by_section != None:
            body['needs_grading_count_by_section'] = self.needs_grading_count_by_section
        if self.bucket != None:
            body['bucket'] = self.bucket
        if self.assingment_ids != None:
            body['assignment_ids[]'] = self.assingment_ids
        if self.order_by != None:
            body['order_by'] = self.order_by
        if self.post_to_sis != None:
            body['post_to_sis'] = self.post_to_sis
        if self.all_dates != None:
            body['all_dates'] = self.all_dates
        if self.assignment_name is not None:
            body['assignment[name'] = self.assignment_name
        if self.assignment_position is not None:
            body['assignment[position]'] = self.assignment_position
        if self.assignment_submission_types is not None:
            body['assignment[submission_types][]'] = self.assignment_submission_types
        if self.assignment_allowed_extensions is not None:
            body['assignment[allowed_extensions][]'] = self.assignment_allowed_extensions
        if self.turnitin_enabled is not None:
            body['assignment[turnitin_enabled]'] = self.turnitin_enabled
        if self.vericite_enabled is not None:
            body['assignment[vericite_enabled]'] = self.vericite_enabled
        if self.turnitin_settings is not None:
            body['assignment[turnitin_settings]'] = self.turnitin_settings
        if self.integration_data is not None:
            body['assignment[integration_data]'] = self.integration_data
        if self.integration_id is not None:
            body['assignment[integration_id]'] = self.integration_id
        if self.peer_reviews is not None:
            body['assignment[peer_reviews]'] = self.peer_reviews
        if self.automatic_peer_reviews is not None:
            body['assignment[automatic_peer_reviews]'] = self.automatic_peer_reviews
        if self.notify_of_update is not None:
            body['assignment[notify_of_update]'] = self.notify_of_update
        if self.group_category_id is not None:
            body['assignment[group_category_id]'] = self.group_category_id
        if self.grade_group_students_individually is not None:
            body['assignment[grade_group_students_individually]'] = self.grade_group_students_individually
        if self.points_possible is not None:
            body['assignment[points_possible]'] = self.points_possible
        if self.grading_type is not None:
            body['assignment[grading_type]'] = self.grading_type
        if self.due_at is not None:
            body['assignment[due_at]'] = self.due_at
        if self.lock_at is not None:
            body['assignment[lock_at]'] = self.lock_at
        if self.unlock_at is not None:
            body['assignment[unlock_at]'] = self.unlock_at
        if self.description is not None:
            body['assignment[description]'] = self.description
        if self.assignment_group_id is not None:
            body['assignment[assignment_group_id]'] = self.assignment_group_id
        if self.assignment_overrides is not None:
            body['assignment[assignment_overrides][]'] = self.assignment_overrides
        if self.only_visible_to_overrides is not None:
            body['assignment[only_visible_to_overrides]'] = self.only_visible_to_overrides
        if self.published is not None:
            body['assignment[published]'] = self.published
        if self.grading_standard_id is not None:
            body['assignment[grading_standard_id]'] = self.grading_standard_id
        if self.omit_from_final_grade is not None:
            body['assignment[omit_from_final_grade]'] = self.omit_from_final_grade
        if self.quiz_lti is not None:
            body['assignment[quiz_lti]'] = self.quiz_lti
        if self.moderated_grading is not None:
            body['assignment[moderated_grading]'] = self.moderated_grading
        if self.grader_count is not None:
            body['assignment[grader_count]'] = self.grader_count
        if self.final_grader_id is not None:
            body['assignment[final_grader_id]'] = self.final_grader_id
        if self.grader_comments_visible_to_graders is not None:
            body['assignment[grader_comments_visible_to_graders]'] = self.grader_comments_visible_to_graders
        if self.graders_anonymous_to_graders is not None:
            body['assignment[graders_anonymous_to_graders]'] = self.graders_anonymous_to_graders
        if self.graders_names_visible_to_final_grader is not None:
            body['assignment[graders_names_visible_to_final_grader]'] = self.graders_names_visible_to_final_grader
        if self.anonymous_grading is not None:
            body['assignment[anonymous_grading]'] = self.anonymous_grading
        if self.allowed_attempts is not None:
            body['assignment[allowed_attempts]'] = self.allowed_attempts
        if self.annotatable_attachment_id is not None:
            body['assignment[annotatable_attachment_id]'] = self.annotatable_attachment_id
        return body
