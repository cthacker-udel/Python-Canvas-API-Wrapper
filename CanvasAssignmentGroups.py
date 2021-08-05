from CanvasClient import CanvasClient


class CanvasAssignmentGroups(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.include = None
        self.assignment_ids = None
        self.exclude_assignment_submission_types = None
        self.override_assignment_dates = None
        self.grading_period_id = None
        self.scope_assignments_to_student = None
        self.assignment_group_id = None

        self.name = None
        self.position = None
        self.group_weight = None
        self.sis_source_id = None
        self.integration_data = None
        self.rules = None

        self.move_assignments_to = None

    def generate_queries(self):

        body = {}
        if self.move_assignments_to != None:
            body['move_assignments_to'] = self.move_assignments_to
        if self.name != None:
            body['name'] = self.name
        if self.position != None:
            body['position'] = self.position
        if self.group_weight != None:
            body['group_weight'] = self.group_weight
        if self.sis_source_id != None:
            body['sis_source_id'] = self.sis_source_id
        if self.integration_data != None:
            body['integration_data'] = self.integration_data
        if self.rules != None:
            body['rules'] = self.rules
        if self.include != None:
            body['include[]'] = self.include
        if self.assignment_ids != None:
            body['assignment_ids[]'] = self.assignment_ids
        if self.exclude_assignment_submission_types != None:
            body['exclude_assignment_submission_types[]'] = self.exclude_assignment_submission_types
        if self.override_assignment_dates != None:
            body['override_assignment_dates'] = self.override_assignment_dates
        if self.grading_period_id != None:
            body['grading_period_id'] = self.grading_period_id
        if self.scope_assignments_to_student != None:
            body['scope_assignments_to_student'] = self.scope_assignments_to_student
        return body

    def clear_queries(self):

        self.include = None
        self.assignment_ids = None
        self.exclude_assignment_submission_types = None
        self.override_assignment_dates = None
        self.grading_period_id = None
        self.scope_assignments_to_student = None
        self.assignment_group_id = None
        self.name = None
        self.position = None
        self.group_weight = None
        self.sis_source_id = None
        self.integration_data = None
        self.rules = None
        self.move_assignments_to = None