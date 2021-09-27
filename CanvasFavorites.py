from CanvasClient import CanvasClient

class CanvasFavorite(CanvasClient):

    def __init__(self):

        self.exclude_blueprint_courses = None
        self.course_id = None
        self.id = None
        self.group_id = None

    def generate_queries(self):

        body = {}

        if self.exclude_blueprint_courses is not None:
            body['exclude_blueprint_courses'] = self.exclude_blueprint_courses
        if self.id is not None:
            body['id'] = self.id
        return body

    def clear_queries(self):

        self.exclude_blueprint_courses = None
        self.course_id = None
        self.id = None
        self.group_id = None