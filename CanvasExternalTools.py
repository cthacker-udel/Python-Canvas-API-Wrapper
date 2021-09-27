from CanvasClient import CanvasClient

class CanvasExternalTools(CanvasClient):

    def __init__(self):

        self.course_id = None
        self.account_id = None
        self.group_id = None
        self.search_term = None
        self.selectable = None
        self.include_parents = None

        self.id = None
        self.url = None
        self.assignment_id = None
        self.module_item_id = None
        self.launch_type = None

        self.external_tool_id = None

        self.name = None
        self.privacy_level = None
        self.consumer_key = None
        self.shared_secret = None
        self.description = None
        self.domain = None
        self.icon_url = None
        self.text = None
        self.custom_fields_field_name = None
        self.account_navigation_url = None
        self.account_navigation_enabled = None
        self.account_navigation_text = None
        self.account_navigation_selection_width = None
        self.account_navigation_selection_height = None
        self.account_navigation_display_type = None
        self.user_navigation_url = None
        self.user_navigation_enabled = None
        self.user_navigation_text = None
        self.user_navigation_visibility = None
        self.course_home_sub_navigation_url = None
        self.course_home_sub_navigation_enabled = None
        self.course_home_sub_navigation_text = None
        self.course_home_sub_navigation_icon_url = None
        self.course_navigation_enabled = None
        self.course_navigation_text = None
        self.course_navigation_visibility = None
        self.course_navigation_window_target = None
        self.course_navigation_default = None
        self.course_navigation_display_type = None
        self.editor_button_url = None
        self.editor_button_enabled = None
        self.editor_button_icon_url = None
        self.editor_button_selection_width = None
        self.editor_button_selection_height = None
        self.editor_button_message_type = None
        self.homework_submission_url = None
        self.homework_submission_enabled = None
        self.homework_submission_text = None
        self.homework_submission_message_type = None
        self.link_selection_url = None
        self.link_selection_enabled = None
        self.link_selection_text = None
        self.link_selection_message_type = None
        self.migration_selection_url = None
        self.migration_selection_enabled = None
        self.migration_selection_message_type = None
        self.tool_configuration_url = None
        self.tool_configuration_enabled = None
        self.tool_configuration_message_type = None
        self.tool_configuration_prefer_sis_email = None
        self.resource_selection_url = None
        self.resource_selection_enabled = None
        self.resource_selection_icon_url = None
        self.resource_selection_selection_width = None
        self.resource_selection_selection_height = None
        self.config_type = None
        self.config_xml = None
        self.config_url = None
        self.not_selectable = None
        self.oauth_compliant = None

        self.rce_favorite_id = None


    def generate_queries(self):

        body = {}

        if self.name is not None:
            body['name'] = self.name
        if self.privacy_level is not None:
            body['privacy_level'] = self.privacy_level
        if self.consumer_key is not None:
            body['consumer_key'] = self.consumer_key
        if self.shared_secret is not None:
            body['shared_secret'] = self.shared_secret
        if self.description is not None:
            body['description'] = self.description
        if self.url is not None:
            body['url'] = self.url
        if self.domain is not None:
            body['domain'] = self.domain
        if self.icon_url is not None:
            body['icon_url'] = self.icon_url
        if self.text is not None:
            body['text'] = self.text
        if self.custom_fields_field_name is not None:
            body['custom_fields[field_name]'] = self.custom_fields_field_name
        if self.account_navigation_url is not None:
            body['account_navigation[url]'] = self.account_navigation_url
        if self.account_navigation_text is not None:
            body['account_navigation[text]'] = self.account_navigation_text
        if self.account_navigation_selection_width is not None:
            body['account_navigation[selection_width]'] = self.account_navigation_selection_width
        if self.account_navigation_selection_height is not None:
            body['account_navigation[selection_height]'] = self.account_navigation_selection_height
        if self.account_navigation_display_type is not None:
            body['account_navigation[display_type]'] = self.account_navigation_display_type
        if self.user_navigation_url is not None:
            body['user_navigation[url]'] = self.user_navigation_url
        if self.user_navigation_enabled is not None:
            body['user_navigation[enabled]'] = self.user_navigation_enabled
        if self.user_navigation_text is not None:
            body['user_navigation[text]'] = self.user_navigation_text
        if self.user_navigation_visibility is not None:
            body['user_navigation[visibility]'] = self.user_navigation_visibility
        if self.course_home_sub_navigation_url is not None:
            body['course_home_sub_navigation[url]'] = self.course_home_sub_navigation_url
        if self.course_home_sub_navigation_enabled is not None:
            body['course_home_sub_navigation[enabled]'] = self.course_home_sub_navigation_enabled
        if self.course_home_sub_navigation_text is not None:
            body['course_home_sub_navigation[text]'] = self.course_home_sub_navigation_text
        if self.course_home_sub_navigation_icon_url is not None:
            body['course_home_sub_navigation[icon_url]'] = self.course_home_sub_navigation_icon_url
        if self.course_navigation_enabled is not None:
            body['course_navigation[enabled]'] = self.course_navigation_enabled
        if self.course_navigation_text is not None:
            body['course_navigation[text]'] = self.course_navigation_text
        if self.course_navigation_visibility is not None:
            body['course_navigation[visibility]'] = self.course_navigation_visibility
        if self.course_navigation_window_target is not None:
            body['course_navigation[windowTarget]'] = self.course_navigation_window_target
        if self.course_navigation_default is not None:
            body['course_navigation[default]'] = self.course_navigation_default
        if self.course_navigation_display_type is not None:
            body['course_navigation[display_type]'] = self.course_navigation_display_type
        if self.editor_button_url is not None:
            body['editor_button[url]'] = self.editor_button_url
        if self.editor_button_enabled is not None:
            body['editor_button[enabled]'] = self.editor_button_enabled
        if self.editor_button_icon_url is not None:
            body['editor_button[icon_url]'] = self.editor_button_icon_url
        if self.editor_button_selection_width is not None:
            body['editor_button[selection_width]'] = self.editor_button_selection_width
        if self.editor_button_selection_height is not None:
            body['editor_button[selection_height]'] = self.editor_button_selection_height
        if self.editor_button_message_type is not None:
            body['editor_button[message_type]'] = self.editor_button_message_type
        if self.homework_submission_url is not None:
            body['homework_submisison[url]'] = self.homework_submission_url
        if self.homework_submission_enabled is not None:
            body['homework_submission[enabled]'] = self.homework_submission_enabled
        if self.homework_submission_text is not None:
            body['homework_submission[text]'] = self.homework_submission_text
        if self.homework_submission_message_type is not None:
            body['homework_submission[message_type]'] = self.homework_submission_message_type
        if self.link_selection_url is not None:
            body['link_selection[url]'] = self.link_selection_url
        if self.link_selection_enabled is not None:
            body['link_selection[enabled]'] = self.link_selection_enabled
        if self.link_selection_text is not None:
            body['link_selection[text]'] = self.link_selection_text
        if self.link_selection_message_type is not None:
            body['link_selection[message_type]'] = self.link_selection_message_type
        if self.migration_selection_url is not None:
            body['migration_selection[url]'] = self.migration_selection_url
        if self.migration_selection_enabled is not None:
            body['migration_selection[enabled]'] = self.migration_selection_enabled
        if self.migration_selection_message_type is not None:
            body['migration_selection[message_type]'] = self.migration_selection_message_type
        if self.tool_configuration_url is not None:
            body['tool_configuration[url]'] = self.tool_configuration_url
        if self.tool_configuration_enabled is not None:
            body['tool_configuration[enabled]'] = self.tool_configuration_enabled
        if self.tool_configuration_message_type is not None:
            body['tool_configuration[message_type]'] = self.tool_configuration_message_type
        if self.tool_configuration_prefer_sis_email is not None:
            body['tool_configuration[prefer_sis_email]'] = self.tool_configuration_prefer_sis_email
        if self.resource_selection_url is not None:
            body['resource_selection[url]'] = self.resource_selection_url
        if self.resource_selection_enabled is not None:
            body['resource_selection[enabled]'] = self.resource_selection_enabled
        if self.resource_selection_icon_url is not None:
            body['resource_selection[icon_url]'] = self.resource_selection_icon_url
        if self.resource_selection_selection_width is not None:
            body['resource_selection[selection_width]'] = self.resource_selection_selection_width
        if self.resource_selection_selection_height is not None:
            body['resource_selection[selection_height]'] = self.resource_selection_selection_height
        if self.config_type is not None:
            body['config_type'] = self.config_type
        if self.config_xml is not None:
            body['config_xml'] = self.config_xml
        if self.config_url is not None:
            body['config_url'] = self.config_url
        if self.not_selectable is not None:
            body['not_selectable'] = self.not_selectable
        if self.oauth_compliant is not None:
            body['oauth_compliant'] = self.oauth_compliant
        if self.id is not None:
            body['id'] = self.id
        if self.url is not None:
            body['url'] = self.url
        if self.assignment_id is not None:
            body['assignment_id'] = self.assignment_id
        if self.module_item_id is not None:
            body['module_item_id'] = self.module_item_id
        if self.launch_type is not None:
            body['launch_type'] = self.launch_type
        if self.search_term is not None:
            body['search_term'] = self.search_term
        if self.selectable is not None:
            body['selectable'] = self.selectable
        if self.include_parents is not None:
            body['include_parents'] = self.include_parents
        return body

    def clear_queries(self):

        self.search_term = None
        self.selectable = None
        self.include_parents = None
        self.id = None
        self.url = None
        self.assingment_id = None
        self.module_item_id = None
        self.launch_type = None
        self.external_tool_id = None
        self.name = None
        self.privacy_level = None
        self.consumer_key = None
        self.shared_secret = None
        self.description = None
        self.domain = None
        self.icon_url = None
        self.text = None
        self.custom_fields_field_name = None
        self.account_navigation_url = None
        self.account_navigation_enabled = None
        self.account_navigation_text = None
        self.account_navigation_selection_width = None
        self.account_navigation_selection_height = None
        self.account_navigation_display_type = None
        self.user_navigation_url = None
        self.user_navigation_enabled = None
        self.user_navigation_text = None
        self.user_navigation_visibility = None
        self.course_home_sub_navigation_url = None
        self.course_home_sub_navigation_enabled = None
        self.course_home_sub_navigation_text = None
        self.course_home_sub_navigation_icon_url = None
        self.course_navigation_enabled = None
        self.course_navigation_text = None
        self.course_navigation_visibility = None
        self.course_navigation_window_target = None
        self.course_navigation_default = None
        self.course_navigation_display_type = None
        self.editor_button_url = None
        self.editor_button_enabled = None
        self.editor_button_icon_url = None
        self.editor_button_selection_width = None
        self.editor_button_selection_height = None
        self.editor_button_message_type = None
        self.homework_submission_url = None
        self.homework_submission_enabled = None
        self.homework_submission_text = None
        self.homework_submission_message_type = None
        self.link_selection_url = None
        self.link_selection_enabled = None
        self.link_selection_text = None
        self.link_selection_message_type = None
        self.migration_selection_url = None
        self.migration_selection_enabled = None
        self.migration_selection_message_type = None
        self.tool_configuration_url = None
        self.tool_configuration_enabled = None
        self.tool_configuration_message_type = None
        self.tool_configuration_prefer_sis_email = None
        self.resource_selection_url = None
        self.resource_selection_enabled = None
        self.resource_selection_icon_url = None
        self.resource_selection_selection_width = None
        self.resource_selection_selection_height = None
        self.config_type = None
        self.config_xml = None
        self.config_url = None
        self.not_selectable = None
        self.oauth_compliant = None
        self.rce_favorite_id = None