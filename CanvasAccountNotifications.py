from CanvasClient import CanvasClient

class CanvasAccountNotifications(CanvasClient):

    def __init__(self):
        self.include_past = None
        self.account_id = None
        self.account_notification_id = None
        self.account_notification_subject = None
        self.account_notification_message = None
        self.account_notification_start_at = None
        self.account_notification_end_at = None
        self.account_notification_icon = None
        self.account_notification_roles = []

    def generate_queries(self):

        body = {}

        if self.include_past != None:
            body['include_past'] = self.include_past
        if self.account_notification_subject != None:
            body['account_notification[subject]'] = self.account_notification_subject
        if self.account_notification_message != None:
            body['account_notification[message]'] = self.account_notification_message
        if self.account_notification_start_at != None:
            body['account_notification[start_at]'] = self.account_notification_start_at
        if self.account_notification_end_at != None:
            body['account_notification[end_at]'] = self.account_notification_end_at
        if self.account_notification_icon != None:
            body['account_notification[icon]'] = self.account_notification_icon
        if len(self.account_notification_roles) > 0:
            body['account_notification_roles[]'] = self.account_notification_roles
        return body

    def clear_queries(self):

        self.include_past = None
        self.account_id = None
        self.account_notification_id = None
        self.account_notification_subject = None
        self.account_notification_message = None
        self.account_notification_start_at = None
        self.account_notification_end_at = None
        self.account_notification_icon = None
        self.account_notification_roles = []