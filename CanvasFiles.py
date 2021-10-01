from CanvasClient import CanvasClient

class CanvasFile(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.group_id = None
        self.user_id = None
        self.folder_id = None
        self.file_id = None

        self.content_types = None
        self.exclude_content_types = None
        self.search_term = None
        self.include = None
        self.only = None
        self.sort = None
        self.order = None
        self.submission_id = None
        self.include = None

        self.name = None
        self.parent_folder_id = None
        self.on_duplicate = None
        self.lock_at = None
        self.unlock_at = None
        self.locked = None
        self.hidden = None
        self.replace = None

        self.folder_full_path = None
        self.position = None
        self.parent_folder_path = None
        self.force = None
        self.source_file_id = None
        self.source_folder_id = None

        self.file_ids = None
        self.folder_ids = None
        self.publish = None

        self.usage_rights_justification = None
        self.usage_rights_copyright = None
        self.usage_rights_license = None

    def generate_queries(self):

        body = {}

        if self.content_types is not None:
            body['content_types[]'] = self.content_types
        if self.exclude_content_types is not None:
            body['exclude_content_types[]'] = self.exclude_content_types
        if self.search_term is not None:
            body['search_term'] = self.search_term
        if self.include is not None:
            body['include[]'] = self.include
        if self.only is not None:
            body['only[]'] = self.only
        if self.sort is not None:
            body['sort'] = self.sort
        if self.order is not None:
            body['order'] = self.order
        if self.submission_id is not None:
            body['submission_id'] = self.submission_id
        if self.name is not None:
            body['name'] = self.name
        if self.parent_folder_id is not None:
            body['parent_folder_id'] = self.parent_folder_id
        if self.on_duplicate is not None:
            body['on_duplicate'] = self.on_duplicate
        if self.lock_at is not None:
            body['lock_at'] = self.lock_at
        if self.unlock_at is not None:
            body['unlock_at'] = self.unlock_at
        if self.locked is not None:
            body['locked'] = self.locked
        if self.hidden is not None:
            body['hidden'] = self.hidden
        if self.replace is not None:
            body['replace'] = self.replace
        if self.position is not None:
            body['position'] = self.position
        if self.parent_folder_path is not None:
            body['parent_folder_path'] = self.parent_folder_path
        if self.force is not None:
            body['force'] = self.force
        if self.file_ids is not None:
            body['file_ids[]'] = self.file_ids
        if self.folder_ids is not None:
            body['folder_ids[]'] = self.folder_ids
        if self.publish is not None:
            body['publish'] = self.publish
        if self.usage_rights_justification is not None:
            body['usage_rights[use_justification]'] = self.usage_rights_justification
        if self.usage_rights_copyright is not None:
            body['usage_rights[legal_copyright]'] = self.usage_rights_copyright
        if self.usage_rights_license is not None:
            body['usage_rights[license]'] = self.usage_rights_license

    def clear_queries(self):

        self.course_id = None
        self.group_id = None
        self.user_id = None
        self.folder_id = None
        self.file_id = None

        self.content_types = None
        self.exclude_content_types = None
        self.search_term = None
        self.include = None
        self.only = None
        self.sort = None
        self.order = None
        self.submission_id = None
        self.include = None

        self.name = None
        self.parent_folder_id = None
        self.on_duplicate = None
        self.lock_at = None
        self.unlock_at = None
        self.locked = None
        self.hidden = None
        self.replace = None

        self.folder_full_path = None
        self.position = None
        self.parent_folder_path = None
        self.force = None
        self.source_file_id = None
        self.source_folder_id = None

        self.file_ids = None
        self.folder_ids = None
        self.publish = None

        self.usage_rights_justification = None
        self.usage_rights_copyright = None
        self.usage_rights_license = None

