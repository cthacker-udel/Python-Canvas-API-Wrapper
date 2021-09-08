from CanvasClient import CanvasClient

class CanvasDiscussionTopics(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.group_id = None

        self.include = None
        self.order_by = None
        self.scope = None
        self.only_announcements = None
        self.filter_by = None
        self.search_term = None
        self.exclude_content_module_locked_topics = None

        self.title = None
        self.message = None
        self.discussion_type = None
        self.published = None
        self.delayed_post_at = None
        self.allow_rating = None
        self.lock_at = None
        self.podcast_enabled = None
        self.podcast_has_student_posts = None
        self.require_initial_post = None
        self.assignment = None
        self.is_announcement = None
        self.pinned = None
        self.position_after = None
        self.group_category_id = None
        self.only_graders_can_rate = None
        self.sort_by_rating = None
        self.attachment = None
        self.specific_sections = None

        self.ids = None
        self.forced_read_state = None
        self.rating = None

        self.discussion_topic_id = None

    def generate_queries(self):

        body = {}

        if self.include is not None:
            body['include'] = self.include
        if self.order_by is not None:
            body['order_by'] = self.order_by
        if self.scope is not None:
            body['scope'] = self.scope
        if self.only_announcements is not None:
            body['only_announcements'] = self.only_announcements
        if self.filter_by is not None:
            body['filter_by'] = self.filter_by
        if self.search_term is not None:
            body['search_term'] = self.search_term
        if self.exclude_content_module_locked_topics is not None:
            body['exclude_context_module_locked_topics'] = self.exclude_content_module_locked_topics
        if self.title is not None:
            body['title'] = self.title
        if self.message is not None:
            body['message'] = self.message
        if self.discussion_type is not None:
            body['discussion_type'] = self.discussion_type
        if self.published is not None:
            body['published'] = self.published
        if self.delayed_post_at is not None:
            body['delayed_post_at'] = self.delayed_post_at
        if self.allow_rating is not None:
            body['allow_rating'] = self.allow_rating
        if self.lock_at is not None:
            body['lock_at'] = self.lock_at
        if self.podcast_enabled is not None:
            body['podcast_enabled'] = self.podcast_enabled
        if self.podcast_has_student_posts is not None:
            body['podcast_has_student_posts'] = self.podcast_has_student_posts
        if self.require_initial_post is not None:
            body['require_initial_post'] = self.require_initial_post
        if self.assignment is not None:
            body['assignment'] = self.assignment
        if self.is_announcement is not None:
            body['is_announcement'] = self.is_announcement
        if self.pinned is not None:
            body['pinned'] = self.pinned
        if self.position_after is not None:
            body['position_after'] = self.position_after
        if self.group_category_id is not None:
            body['group_category_id'] = self.group_category_id
        if self.only_graders_can_rate is not None:
            body['only_graders_can_rate'] = self.only_graders_can_rate
        if self.sort_by_rating is not None:
            body['sort_by_rating'] = self.sort_by_rating
        if self.attachment is not None:
            body['attachment'] = self.attachment
        if self.specific_sections is not None:
            body['specific_sections'] = self.specific_sections
        return body

    def clear_queries(self):
        self.course_id = None
        self.group_id = None

        self.include = None
        self.order_by = None
        self.scope = None
        self.only_announcements = None
        self.filter_by = None
        self.search_term = None
        self.exclude_content_module_locked_topics = None

        self.title = None
        self.message = None
        self.discussion_type = None
        self.published = None
        self.delayed_post_at = None
        self.allow_rating = None
        self.lock_at = None
        self.podcast_enabled = None
        self.podcast_has_student_posts = None
        self.require_initial_post = None
        self.assignment = None
        self.is_announcement = None
        self.pinned = None
        self.position_after = None
        self.group_category_id = None
        self.only_graders_can_rate = None
        self.sort_by_rating = None
        self.attachment = None
        self.specific_sections = None

        self.ids = None
        self.forced_read_state = None
        self.rating = None

        self.discussion_topic_id = None
