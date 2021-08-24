from CanvasClient import CanvasClient

class CanvasContentMigration(CanvasClient):

    def __init__(self):

        self.account_id = None
        self.course_id = None
        self.group_id = None
        self.user_id = None
        self.content_migration_id = None
        self.migration_issue_id = None

        self.workflow_state = None

        self.migration_type = None
        self.preattach_name = None
        self.preattacfh_prop = None
        self.preattach_url = None
        self.settings_export_id = None
        self.settings_source_id = None
        self.settings_folder_id = None
        self.settings_overwrite_quizzes = None
        self.settings_question_bank_id = None
        self.settings_question_bank_name = None
        self.settings_insert_into_module_id = None
        self.settings_insert_into_module_type = None
        self.settings_insert_into_module_position = None
        self.settings_move_to_assignment_group_id = None

        self.ds_options_shift_dates = None
        self.ds_options_old_start_date = None
        self.ds_options_old_end_date = None
        self.ds_options_new_start_date = None
        self.ds_options_new_end_date = None
        self.ds_options_day_substitutions =  None
        self.ds_options_remove_dates = None

        self.selective_import = None
        self.select = None

        self.type = None


    def generate_queries(self):

        body = {}

        if self.workflow_state is not None:
            body['workflow_state'] = self.workflow_state
        if self.migration_type is not None:
            body['migration_type'] = self.migration_type
        if self.preattach_name is not None:
            body['pre_attachment[name]'] = self.preattach_name
        if self.preattacfh_prop is not None:
            body['pre_attachment[*]'] = self.preattacfh_prop
        if self.preattach_url is not None:
            body['settings[file_url]'] = self.preattach_url
        if self.settings_export_id is not None:
            body['settings[content_export_id]'] = self.settings_export_id
        if self.settings_source_id is not None:
            body['settings[source_course_id]'] = self.settings_source_id
        if self.settings_folder_id is not None:
            body['settings[folder_id]'] = self.settings_folder_id
        if self.settings_overwrite_quizzes is not None:
            body['settings[overwrite_quizzes]'] = self.settings_overwrite_quizzes
        if self.settings_question_bank_id is not None:
            body['settings[question_bank_id]'] = self.settings_question_bank_id
        if self.settings_question_bank_name is not None:
            body['settings[question_bank_name]'] = self.settings_question_bank_name
        if self.settings_insert_into_module_id is not None:
            body['settings[insert_into_module_id]'] = self.settings_insert_into_module_id
        if self.settings_insert_into_module_type is not None:
            body['settings[insert_into_module_type]'] = self.settings_insert_into_module_type
        if self.settings_insert_into_module_position is not None:
            body['settings[insert_into_module_position]'] = self.settings_insert_into_module_position
        if self.settings_move_to_assignment_group_id is not None:
            body['settings[move_to_assignment_group_id]'] = self.settings_move_to_assignment_group_id
        if self.ds_options_shift_dates is not None:
            body['date_shift_options[shift_dates]'] = self.ds_options_shift_dates
        if self.ds_options_old_start_date is not None:
            body['date_shift_options[old_start_date]'] = self.ds_options_old_start_date
        if self.ds_options_old_end_date is not None:
            body['date_shift_options[old_end_date]'] = self.ds_options_old_end_date
        if self.ds_options_new_start_date is not None:
            body['date_shift_options[new_start_date]'] = self.ds_options_new_start_date
        if self.ds_options_new_end_date is not None:
            body['date_shift_options[new_end_date]'] = self.ds_options_new_end_date
        if self.ds_options_day_substitutions is not None:
            body['date_shift_options[day_substitutions][X]'] = self.ds_options_day_substitutions
        if self.ds_options_remove_dates is not None:
            body['date_shift_options[remove_dates]'] = self.ds_options_remove_dates
        if self.selective_import is not None:
            body['selective_import'] = self.selective_import
        if self.select is not None:
            body['select'] = self.select
        if self.type is not None:
            body['type'] = self.type
        return body


    def clear_queries(self):
        self.account_id = None
        self.course_id = None
        self.group_id = None
        self.user_id = None
        self.content_migration_id = None
        self.migration_issue_id = None

        self.workflow_state = None

        self.migration_type = None
        self.preattach_name = None
        self.preattacfh_prop = None
        self.preattach_url = None
        self.settings_export_id = None
        self.settings_source_id = None
        self.settings_folder_id = None
        self.settings_overwrite_quizzes = None
        self.settings_question_bank_id = None
        self.settings_question_bank_name = None
        self.settings_insert_into_module_id = None
        self.settings_insert_into_module_type = None
        self.settings_insert_into_module_position = None
        self.settings_move_to_assignment_group_id = None

        self.ds_options_shift_dates = None
        self.ds_options_old_start_date = None
        self.ds_options_old_end_date = None
        self.ds_options_new_start_date = None
        self.ds_options_new_end_date = None
        self.ds_options_day_substitutions = None
        self.ds_options_remove_dates = None

        self.selective_import = None
        self.select = None

        self.type = None