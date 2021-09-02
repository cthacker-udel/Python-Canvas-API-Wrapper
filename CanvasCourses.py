from CanvasClient import CanvasClient

class CanvasCourses(CanvasClient):

    def __init__(self):

        self.user_id = None

        self.enrollment_type = None
        self.enrollment_role = None
        self.enrollment_role_id = None
        self.enrollment_state = None
        self.exclude_blueprint_courses = None
        self.include = None
        self.state = None


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