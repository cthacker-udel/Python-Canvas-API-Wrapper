from CanvasClient import CanvasClient


class CanvasCourseQuizExtensions(CanvasClient):

    def __init_(self):

        self.course_id = None
        self.user_id = None
        self.extra_attempts = None
        self.extra_time = None
        self.manually_unlocked = None
        self.extend_from_now = None
        self.extend_from_end_at = None

    def generate_queries(self):

        body = {}

        if self.user_id is not None:
            body['user_id'] = self.user_id
        if self.extra_attempts is not None:
            body['extra_attempts'] = self.extra_attempts
        if self.extra_time is not None:
            body['extra_time'] = self.extra_time
        if self.manually_unlocked is not None:
            body['manually_unlocked'] = self.manually_unlocked
        if self.extend_from_now is not None:
            body['extend_from_now'] = self.extend_from_now
        if self.extend_from_end_at is not None:
            body['extend_from_end_at'] = self.extend_from_end_at
        return body

    def clear_queries(self):

        self.course_id = None
        self.user_id = None
        self.extra_attempts = None
        self.extra_time = None
        self.manually_unlocked = None
        self.extend_from_now = None
        self.extend_from_end_at = None