from CanvasClient import CanvasClient

class CanvasAccount(CanvasClient):

    def __init__(self):

        self.account_id = None
        self.user_id = None
        self.sub_account_id = None

        self.include = None
        self.permissions = None
        self.recursive = None
        self.with_enrollments = None
        self.enrollment_type = None
        self.published = None
        self.completed = None
        self.blueprint = None
        self.blueprint_associated = None
        self.by_teachers = None
        self.by_subaccounts = None
        self.hide_enrollmentless_courses = None
        self.state = None
        self.enrollment_term_id = None
        self.search_term = None
        self.sort = None
        self.order = None
        self.search_by = None
        self.starts_before = None
        self.ends_after = None
        self.homeroom = None

        self.account_name = None
        self.account_sis_account_id = None
        self.account_default_time_zone = None
        self.default_storage_quota_mb = None
        self.default_user_storage_quota_mb = None
        self.default_group_storage_quota_mb = None
        self.course_template_id = None
        self.account_settings_restrict_student_past_view_value = None
        self.account_settings_restrict_student_past_view_locked = None
        self.account_settings_restrict_student_future_view_value = None
        self.account_settings_microsoft_sync_enabled = None
        self.account_settings_microsoft_sync_tenant = None
        self.account_settings_microsoft_sync_login_attribute = None
        self.account_settings_restrict_student_future_view_locked = None
        self.account_settings_lock_all_announcements_value = None
        self.account_settings_lock_all_announcements_locked = None
        self.account_settings_usage_rights_required_value = None
        self.account_settings_usage_rights_required_locked = None
        self.account_settings_restrict_student_future_listing_value = None
        self.account_settings_restrict_student_future_listing_locked = None
        self.account_settings_lock_outcome_proficiency_value = None
        self.account_lock_outcome_proficiency_locked = None
        self.account_settings_lock_proficiency_calculation_value = None
        self.account_lock_proficiency_calculation_locked = None
        self.account_services = None


    def generate_queires(self):

        body = {}

        if self.with_enrollments != None:
            body['with_enrollments'] = self.with_enrollments
        if self.enrollment_type != None:
            body['enrollment_type[]'] = self.enrollment_type
        if self.published != None:
            body['published'] = self.published
        if self.completed != None:
            body['completed'] = self.completed
        if self.blueprint != None:
            body['blueprint'] = self.blueprint
        if self.blueprint_associated != None:
            body['blueprint_associated'] = self.blueprint_associated
        if self.by_teachers != None:
            body['by_teachers[]'] = self.by_teachers
        if self.by_subaccounts != None:
            body['by_subaccounts[]'] = self.by_subaccounts
        if self.hide_enrollmentless_courses != None:
            body['hide_enrollmentless_courses'] = self.hide_enrollmentless_courses
        if self.state != None:
            body['state[]'] = self.state
        if self.enrollment_term_id != None:
            body['enrollment_term_id'] = self.enrollment_term_id
        if self.search_term != None:
            body['search_term'] = self.search_term
        if self.include != None:
            body['include[]'] = self.include
        if self.sort != None:
            body['sort'] = self.sort
        if self.order != None:
            body['order'] = self.order
        if self.search_by != None:
            body['search_by'] = self.search_by
        if self.starts_before != None:
            body['starts_before'] = self.starts_before
        if self.ends_after != None:
            body['ends_after'] = self.ends_after
        if self.homeroom != None:
            body['homeroom'] = self.homeroom
        if self.account_name != None:
            body['account[name]'] = self.account_name
        if self.account_sis_account_id != None:
            body['account[sis_account_id]'] = self.account_sis_account_id
        if self.account_default_time_zone != None:
            body['account[default_time_zone]'] = self.account_default_time_zone
        if self.default_storage_quota_mb != None:
            body['account[default_storeage_quota_mb]'] = self.default_storage_quota_mb
        if self.default_user_storage_quota_mb != None:
            body['account[default_user_storage_quota_mb]'] = self.default_user_storage_quota_mb
        if self.default_group_storage_quota_mb != None:
            body['account[default_group_storage_quota_mb]'] = self.default_group_storage_quota_mb
        if self.course_template_id != None:
            body['account[course_template_id]'] = self.course_template_id
        if self.account_settings_restrict_student_past_view_value != None:
            body['account[settings][restrict_student_past_view][value]'] = self.account_settings_restrict_student_past_view_value
        if self.account_settings_restrict_student_past_view_locked != None:
            body['account[settings][restrict_student_past_view][locked]'] = self.account_settings_restrict_student_past_view_locked
        if self.account_settings_restrict_student_future_view_value != None:
            body['account[settings][restrict_student_future_view][value]'] = self.account_settings_restrict_student_future_view_value
        if self.account_settings_microsoft_sync_enabled != None:
            body['account[settings][microsoft_sync_enabled]'] = self.account_settings_microsoft_sync_enabled
        if self.account_settings_microsoft_sync_tenant != None:
            body['account[settings][microsoft_sync_tenant]'] = self.account_settings_microsoft_sync_tenant
        if self.account_settings_microsoft_sync_login_attribute != None:
            body['account[settings][microsoft_sync_login_attribute]'] = self.account_settings_microsoft_sync_login_attribute
        if self.account_settings_restrict_student_future_view_locked != None:
            body['account[settings][restrict_student_future_view][locked]'] = self.account_settings_restrict_student_future_view_locked
        if self.account_settings_lock_all_announcements_locked != None:
            body['account[settings][lock_all_announcements][locked]'] = self.account_settings_lock_all_announcements_locked
        if self.account_settings_lock_all_announcements_value != None:
            body['account[settings][lock_all_announcements][value]'] = self.account_settings_lock_all_announcements_value
        if self.account_settings_usage_rights_required_value != None:
            body['account[settings][usage_rights_required][value]'] = self.account_settings_usage_rights_required_value
        if self.account_settings_usage_rights_required_locked != None:
            body['account[settings][usage_rights_required][locked]'] = self.account_settings_usage_rights_required_locked
        if self.account_settings_restrict_student_future_listing_value != None:
            body['account[settings][restrict_student_future_listing][value]'] = self.account_settings_restrict_student_future_view_value
        if self.account_settings_restrict_student_future_listing_locked != None:
            body['account[settings][restrict_student_future_listing][locked]'] = self.account_settings_restrict_student_future_listing_locked
        if self.account_settings_lock_outcome_proficiency_value != None:
            body['account[settings][lock_outcome_proficiency][value]'] = self.account_settings_lock_outcome_proficiency_value
        if self.account_lock_outcome_proficiency_locked != None:
            body['account[lock_outcome_proficiency][locked]'] = self.account_lock_outcome_proficiency_locked
        if self.account_settings_lock_proficiency_calculation_value != None:
            body['account[settings][lock_proficiency_calculation][value]'] = self.account_settings_lock_proficiency_calculation_value
        if self.account_lock_proficiency_calculation_locked != None:
            body['account[lock_proficiency_calculation][locked]'] = self.account_lock_outcome_proficiency_locked
        if self.account_services != None:
            body['account[services]'] = self.account_services
        return body

    def clear_queries(self):

        self.with_enrollments = None
        self.enrollment_type = None
        self.published = None
        self.completed = None
        self.blueprint = None
        self.blueprint_associated = None
        self.by_teachers = None
        self.by_subaccounts = None
        self.hide_enrollmentless_courses = None
        self.state = None
        self.enrollment_term_id = None
        self.search_term = None
        self.include = None
        self.sort = None
        self.order = None
        self.search_by = None
        self.starts_before = None
        self.ends_after = None
        self.homeroom = None