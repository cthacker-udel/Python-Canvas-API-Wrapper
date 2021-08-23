from CanvasClient import CanvasClient

class CanvasContentExports(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.group_id = None
        self.user_id = None
        self.content_export_id = None

        self.export_type = None
        self.skip_notifications = None
        self.select = None


    def generate_queries(self):

        body = {}

        if self.export_type is not None:
            body['export_type'] = self.export_type
        if self.skip_notifications is not None:
            body['skip_notifications'] = self.skip_notifications
        if self.select is not None:
            body['select'] = self.select
        return body

    def clear_queries(self):

        self.course_id = None
        self.group_id = None
        self.user_id = None
        self.content_export_id = None

        self.export_type = None
        self.skip_notifications = None
        self.select = None