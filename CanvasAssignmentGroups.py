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

    def generate_queries(self):

        body = {}
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