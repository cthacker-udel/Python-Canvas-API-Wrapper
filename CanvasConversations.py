from CanvasClient import CanvasClient

class CanvasConversations(CanvasClient):


    def __init__(self):

        self.conversation_id = None

        self.scope = None
        self.filter = None
        self.filter_mode = None
        self.interleave_submissions = None
        self.include_all_conversation_ids = None
        self.include = None

        self.recipients = None
        self.subject = None
        self.body = None
        self.force_new = None
        self.group_conversation = None
        self.attachment_ids = None
        self.media_comment_id = None
        self.media_comment_type = None
        self.user_note = None
        self.mode = None
        self.context_code = None

        self.auto_mark_as_read = None

        self.conversation_workflow_state = None
        self.conversation_subscribed = None
        self.conversation_starred = None


    def generate_queries(self):

        body = {}

        if self.auto_mark_as_read is not None:
            body['auto_mark_as_read'] = self.auto_mark_as_read
        if self.recipients is not None:
            body['recipients'] = self.recipients
        if self.subject is not None:
            body['subject'] = self.subject
        if self.body is not None:
            body['body'] = self.body
        if self.force_new is not None:
            body['force_new'] = self.force_new
        if self.group_conversation is not None:
            body['group_conversation'] = self.group_conversation
        if self.attachment_ids is not None:
            body['attachment_ids[]'] = self.attachment_ids
        if self.media_comment_type is not None:
            body['media_comment_type'] = self.media_comment_type
        if self.media_comment_id is not None:
            body['media_comment_id'] = self.media_comment_id
        if self.user_note is not None:
            body['user_note'] = self.user_note
        if self.mode is not None:
            body['mode'] = self.mode
        if self.context_code is not None:
            body['context_code'] = self.context_code
        if self.scope is not None:
            body['scope'] = self.scope
        if self.filter is not None:
            body['filter[]'] = self.filter
        if self.filter_mode is not None:
            body['filter_mode'] = self.filter_mode
        if self.interleave_submissions is not None:
            body['interleave_submissions'] = self.interleave_submissions
        if self.include_all_conversation_ids is not None:
            body['include_all_conversation_ids'] = self.include_all_conversation_ids
        if self.include is not None:
            body['include[]'] = self.include
        return body

    def clear_queries(self):

        self.scope = None
        self.filter = None
        self.filter_mode = None
        self.interleave_submissions = None
        self.include_all_conversation_ids = None
        self.include = None
        self.recipients = None
        self.subject = None
        self.body = None
        self.force_new = None
        self.group_conversation = None
        self.attachment_ids = None
        self.media_comment_id = None
        self.media_comment_type = None
        self.user_note = None
        self.mode = None
        self.context_code = None
        self.auto_mark_as_read = None
        self.conversation_id = None