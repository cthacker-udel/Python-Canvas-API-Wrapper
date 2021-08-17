from CanvasClient import CanvasClient

class CanvasBlueprint(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.template_id = None
        self.course_id = None

        self.course_ids_to_add = None
        self.course_ids_to_remove = None

        self.comment = None
        self.send_notification = None
        self.copy_settings = None
        self.publish_after_initial_sync = None

        self.content_type = None
        self.content_id = None
        self.restricted = None
        self.restrictions = None

        self.migration_id = None
        self.subscription_id = None

    def generate_queries(self):

        body = {}

        if self.course_ids_to_add is not None:
            body['course_ids_to_add'] = self.course_ids_to_add
        if self.course_ids_to_remove is not None:
            body['course_ids_to_remove'] = self.course_ids_to_remove
        if self.comment is not None:
            body['comment'] = self.comment
        if self.send_notification is not None:
            body['send_notification'] = self.send_notification
        if self.copy_settings is not None:
            body['copy_settings'] = self.copy_settings
        if self.publish_after_initial_sync is not None:
            body['publish_after_initial_sync'] = self.publish_after_initial_sync
        if self.content_type is not None:
            body['content_type'] = self.content_type
        if self.content_id is not None:
            body['content_id'] = self.content_id
        if self.restricted is not None:
            body['restricted'] = self.restricted
        if self.restrictions is not None:
            body['restrictions'] = self.restrictions
        return body

    def clear_queries(self):

        self.course_id = None
        self.template_id = None
        self.course_id = None

        self.course_ids_to_add = None
        self.course_ids_to_remove = None

        self.comment = None
        self.send_notification = None
        self.copy_settings = None
        self.publish_after_initial_sync = None

        self.content_type = None
        self.content_id = None
        self.restricted = None
        self.restrictions = None