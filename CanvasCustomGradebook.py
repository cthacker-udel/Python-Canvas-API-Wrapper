from CanvasClient import CanvasClient

class CanvasCustomGradebook(CanvasClient):

    def __init__(self):

        self.course_id = None

        self.include_hidden = None

        self.custom_gradebook_column_id = None

        self.column_title = None
        self.column_position = None
        self.column_hidden = None
        self.column_teacher_notes = None
        self.column_read_only = None

        self.order = None
        self.include_hidden = None
        self.column_data_content = None
        self.bulk_column_data = None

    def generate_queries(self):

        body = {}

        if self.include_hidden is not None:
            body['include_hidden'] = self.include_hidden
        if self.column_title is not None:
            body['column[title]'] = self.column_title
        if self.column_position is not None:
            body['column[position]'] = self.column_position
        if self.column_hidden is not None:
            body['column[hidden]'] = self.column_hidden
        if self.column_teacher_notes is not None:
            body['column[teacher_notes]'] = self.column_teacher_notes
        if self.column_read_only is not None:
            body['column[read_only]'] = self.column_read_only
        if self.order is not None:
            body['order[]'] = self.order
        if self.include_hidden is not None:
            body['include_hidden'] = self.include_hidden
        if self.column_data_content is not None:
            body['column_data[content]'] = self.column_data_content
        if self.bulk_column_data is not None:
            body['column_data[]'] = self.bulk_column_data
        return body

    def clear_queries(self):

        self.course_id = None

        self.include_hidden = None

        self.column_title = None
        self.column_position = None
        self.column_hidden = None
        self.column_teacher_notes = None
        self.column_read_only = None

        self.order = None
        self.include_hidden = None
        self.column_data_content = None
        self.bulk_column_data = None