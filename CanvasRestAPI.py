import requests

from CanvasClient import CanvasClient
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from pprint import pprint

class OAuthRequests(CanvasClient):

    def __init__(self,client):
        self.client = client

    def generate_token(self):

        try:
            br = webdriver.Firefox(FirefoxDriverManager.install())
        except Exception as e:
            try:
                br = webdriver.opera(OperaDriverManager.install())
            except Exception as e:
                try:
                    br = webdriver.edge(EdgeChromiumDriverManager.install())
                except Exception as e:
                    try:
                        br = webdriver.chrome(ChromeDriverManager.install())
                    except Exception as e:
                        print('Unable to instantiate browser')

        ###browser initiated

        url = 'https://{}/login/oauth2/auth?client_id={}&response_type=code&state={}&redirect_uri={}'.format(self.install_url,self.client_id,self.state,self.redirect_uri)


        br.get(url)


        ### user accepts, then canvas sends a oauth2 code in the query response



#######################
# API TOKEN SCOPES API
#######################

class CanvasTokenScopes(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_scopes(self):

        url = self.base_url + '/api/v1/accounts/{}/scopes'.format(self.client.CanvasTokenScopes.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasTokenScopes.generate_queries())

        pprint(request)


class CanvasAccountDomainLookup(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def search_account_domains(self):

        url = self.base_url + '/api/v1/accounts/search'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAccountDomainLookup.generate_queries())

        pprint(request)


class CanvasAccountNotifications(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def get_index_of_user_global_notification(self):

        url = self.base_url + '/api/v1/accounts/{}/account_notifications'.format(self.client.CanvasAccountNotifications.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAccountNotifications.generate_queries())

        pprint(request)

    def show_global_notification(self):

        url = self.base_url + '/api/v1/accounts/{}/account_notifications/{}'.format(self.client.CanvasAccountNotifications.account_id,self.client.CanvasAccountNotifications.account_notification_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def close_notification(self):

        url = self.base_url + '/api/v1/accounts/{}/account_notifications/{}'.format(self.client.CanvasAccountNotifications.account_id,self.client.CanvasAccountNotifications.account_notification_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_global_notification(self):

        url = self.base_url + '/api/v1/accounts/{}/account_notifications'.format(self.client.CanvasAccountNotifications.account_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccountNotifications.generate_queries())

        pprint(request)

    def update_global_notification(self):

        url = self.base_url + '/api/v1/accounts/{}/account_notifications/{}'.format(self.client.CanvasAccountNotifications.account_id,self.client.CanvasAccountNotifications.account_notification_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccountNotifications.generate_queries())

        pprint(request)

class CanvasAccountReports(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)


    def list_available_reports(self):

        url = self.base_url + '/api/v1/accounts/{}/reports'.format(self.client.CanvasAccountReport.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def start_report(self):

        url = self.base_url + '/api/v1/accounts/{}/reports/{}'.format(self.client.CanvasAccountReport.account_id,self.client.CanvasAccountReport.report_type)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccountReport.generate_queries())

        pprint(request)

    def index_of_reports(self):

        url = self.base_url + '/api/v1/accounts/{}/reports/{}'.format(self.client.CanvasAccountReport.account_id,self.client.CanvasAccountReport.report_type)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def report_status(self):

        url = self.base_url + '/api/v1/accounts/{}/reports/{}/{}'.format(self.client.CanvasAccountReport.account_id,self.client.CanvasAccountReport.report_type,self.client.CanvasAccountReport.report_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def delete_report(self):

        url = self.base_url + '/api/v1/accounts/{}/reports/{}/{}'.format(self.client.CanvasAccountReport.account_id,self.client.CanvasAccountReport.report_type,self.client.CanvasAccountReport.report_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

class CanvasAccount(CanvasClient):

    def __init__(self,client):

        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_accounts(self):

        url = self.base_url + '/api/v1/accounts'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def get_admin_manageable_accounts(self):

        url = self.base_url + '/api/v1/manageable_accounts'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_course_admin_accounts(self):

        url = self.base_url + '/api/v1/course_accounts'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_account(self):

        url = self.base_url + '/api/v1/accounts/{}'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_account_settings(self):

        url = self.base_url + '/api/v1/accounts/{}/settings'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_account_permissions(self):

        url = self.base_url + '/api/v1/accounts/{}/permissions'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def get_accounts_sub_accounts(self):

        url = self.base_url + '/api/v1/accounts/{}/sub_accounts'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def get_terms_of_service(self):

        url = self.base_url + '/api/v1/accounts/{}/terms_of_service'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_account_help_links(self):

        url = self.base_url + '/api/v1/accounts/{}/help_links'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def list_account_active_courses(self):

        url = self.base_url + '/api/v1/accounts/{}/courses'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_account(self):

        url = self.base_url + '/api/v1/accounts/{}'.format(self.client.CanvasAccount.account_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def delete_root_account_user(self):

        url = self.base_url + '/api/v1/accounts/{}/users/{}'.format(self.client.CanvasAccount.account_id,self.client.CanvasAccount.user_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def create_new_sub_account(self):

        url = self.base_url + '/api/v1/accounts/{}/sub_accounts'.format(self.client.CanvasAccount.account_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def delete_sub_account(self):

        url = self.base_url + '/api/v1/accounts/{}/sub_accounts/{}'.format(self.client.CanvasAccount.account_id,self.client.CanvasAccount.sub_account_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAccount.generate_queries())

        pprint(request)


class CanvasAdmin(CanvasClient):

    def __init__(self,client):

        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def make_account_admin(self):

        url = self.base_url + '/api/v1/accounts/{}/admins'.format(self.client.CanvasAdmin.account_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAdmin.generate_queries())

        pprint(request)

    def remove_account_admin(self):

        url = self.base_url + '/api/v1/accounts/{}/admins/{}'.format(self.client.CanvasAdmin.account_id,self.client.CanvasAdmin.admin_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAdmin.generate_queries())

        pprint(request)

    def list_account_admins(self):

        url = self.base_url + '/api/v1/accounts/{}/admins'.format(self.client.CanvasAdmin.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAdmin.generate_queries())

        pprint(request)


class CanvasAnalytics(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)


    def get_term_department_level_participation_data(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/terms/{}/activity'.format(self.client.CanvasAnalytics.account_id,self.client.CanvasAnalytics.term_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def get_current_department_level_analytics(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/current/activity'.format(self.client.CanvasAnalytics.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_completed_department_level_analytics(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/completed/activity'.format(self.client.CanvasAnalytics.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_term_department_grade_data(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/terms/{}/grades'.format(self.client.CanvasAnalytics.account_id,self.client.CanvasAnalytics.term_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_current_department_grade_data(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/current/grades'.format(self.client.CanvasAnalytics.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_term_department_statistics(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/terms/{}/statistics'.format(self.client.CanvasAnalytics.account_id,self.client.CanvasAnalytics.term_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_current_department_statistics(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/current/statistics'.format(self.client.CanvasAnalytics.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_completed_department_statistics(self):

        url = self.base_url + '/api/v1/accounts/{}/analytics/completed/statistics'.format(self.client.CanvasAnalytics.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_level_participation_data(self):

        url = self.base_url + '/api/v1/courses/{}/analytics/activity'.format(self.client.CanvasAnalytics.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_level_assignment_data(self):

        url = self.base_url + '/api/v1/courses/{}/analytics/assignments'.format(self.client.CanvasAnalytics.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_level_student_summary_data(self):

        url = self.base_url + '/api/v1/courses/{}/analytics/student_summaries'.format(self.client.CanvasAnalytics.course_id)

        request = requests.get(url,auth={'Authorization {}'.format(self.token)},params=self.client.CanvasAnalytics.generate_queries())

        pprint(request)

    def get_user_participation_data(self):

        url = self.base_url + '/api/v1/courses/{}/analytics/users/{}/activity'.format(self.client.CanvasAnalytics.course_id,self.client.CanvasAnalytics.student_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def get_user_assignment_data(self):

        url = self.base_url + '/api/v1/courses/{}/analytics/users/{}/assignments'.format(self.client.CanvasAnalytics.course_id,self.client.CanvasAnalytics.user_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_user_messaging_data(self):

        url = self.base_url + '/api/v1/courses/{}/analytics/users/{}/communication'.format(self.client.CanvasAnalytics.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasExternalFeed(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_external_feed_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/external_feeds'.format(self.client.CanvasExternalFeed.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_external_feed_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/external_feeds'.format(self.client.CanvasExternalFeed.group_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_external_feed_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/external_feeds'

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)


    def create_external_feed_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/external_feeds'.format(self.client.CanvasExternalFeed.group_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)

    def delete_external_feed_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/external_feeds/{}'.format(self.client.CanvasExternalFeed.course_id,self.client.CanvasExternalFeed.external_feed_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)

    def delete_external_feed_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/external_feeds/{}'.format(self.client.CanvasExternalFeed.group_id,self.client.CanvasExternalFeed.external_feed_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)


class CanvasAnnouncement(CanvasClient):

    def __init__(self,client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_announcements(self):

        url = self.base_url + '/api/v1/announcements'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAnnouncements.generate_queries())

        pprint(request)


class CanvasAppointmentGroups(CanvasClient):

    def __init__(self,client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client


    def list_appointment_groups(self):

        url = self.base_url + '/api/v1/appointment_groups'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def create_appointment_group(self):

        url = self.base_url + '/api/v1/appointment_groups'

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def get_single_appointment_group(self):

        url = self.base_url + '/api/v1/appointment_groups/{}'.format(self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def update_appointment_group(self):

        url = self.base_url + '/api/v1/appointment_groups/{}'.format(self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def delete_appointment_group(self):

        url = self.base_url + '/api/v1/appointment_groups/{}'.format(self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def list_user_participants(self):

        url = self.base_url + '/api/v1/appointment_groups/{}/users'.format(self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def list_student_group_participants(self):

        url = self.base_url + '/api/v1/appointment_groups/{}/groups'.format(self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def get_next_appointment(self):

        url = self.base_url + '/api/v1/appointment_groups/next_appointment'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)


class CanvasAssignmentExtensions(CanvasClient):

    def __init__(self,client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def set_extensions_student_assignment_submissions(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}/extensions'.format(self.client.CanvasAssignmentExtensions.course_id,self.client.CanvasAssignmentExtensions.assignment_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAssignmentExtensions.generate_queries())

        pprint(request)


class CanvasAssignmentGroups(CanvasClient):

    def __init__(self,client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_assignment_groups(self):

        url = self.base_url + "/api/v1/courses/{}/assignment_groups".format(self.client.CanvasAssignmentGroups.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.client.CanvasAssignmentGroups.course_id)},data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def get_assignment_group(self):

        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}'.format(self.client.CanvasAssignmentGroups.course_id,self.client.CanvasAssignmentGroups.assignment_group_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def create_assignment_group(self):

        url = self.base_url + '/api/v1/courses/{}/assignment_groups'.format(self.client.CanvasAssignmentGroups.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def edit_assignment_group(self):

        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}'.format(self.client.CanvasAssignmentGroups.course_id,self.client.CanvasAssignmentGroups.assignment_group_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def destroy_assignment_group(self):

        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}'.format(self.client.CanvasAssignmentGroups.course_id,self.client.CanvasAssignmentGroups.assignment_group_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

class CanvasAssignments(CanvasClient):

    def __init__(self,client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def delete_assignment(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_assignments_v1(self):

        url = self.base_url + '/api/v1/courses/{}/assignments'.format(self.client.CanvasAssignments.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def list_assignments_v2(self):

        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}/assignments'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def list_user_assignments(self):

        url = self.base_url + '/api/v1/users/{}/courses/{}/assignments'.format(self.client.CanvasAssignments.user_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def duplicate_assignment(self):

        url = self.base_url + '/api/v1/courses/{}/assingments/{}/duplicate'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def get_single_assignment(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def create_assignment(self):

        url = self.base_url + '/api/v1/courses/{}/assignments'.format(self.client.CanvasAssignments.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def edit_assignment(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def bulk_update_dates(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/bulk_update'.format(self.client.CanvasAssignments.course_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def list_assignment_overrides(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_assignment_override(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides/{}'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id,self.client.CanvasAssignments.override_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def redirect_assignment_override_to_group(self):

        url = self.base_url + '/api/v1/groups/{}/assignments/{}/override'.format(self.client.CanvasAssignments.group_id,self.client.CanvasAssignments.assignment_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def redirect_assignment_override_to_section(self):

        url = self.base_url + '/api/v1/sections/{}/assignments/{}/override'.format(self.client.CanvasAssignments.course_section_id,self.client.CanvasAssignments.assignment_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_assignment_override(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def update_assignment_override(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides/{}'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id,self.client.CanvasAssignments.override_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def delete_assignment_override(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides/{}'.format(self.client.CanvasAssignments.course_id,self.client.CanvasAssignments.assignment_id,self.client.CanvasAssignments.override_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def batch_retrieve_overrides_in_course(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/overrides'.format(self.client.CanvasAssignments.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def batch_create_overrides_in_course(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/overrides'.format(self.client.CanvasAssignments.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def batch_update_overrides_in_course(self):

        url = self.base_url + '/api/v1/courses/{}/assignments/overrides'.format(self.client.CanvasAssignments.course_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

class CanvasAuthenticationProviders(CanvasClient):

    def __init__(self,client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_authentication_providers(self):

        url = self.base_url + '/api/v1/accounts/{}/authentication_providers'.format(self.client.CanvasAuthProvider.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def add_authentication_provider(self):

        url = self.base_url + '/api/v1/accounts/{}/authentication_providers'.format(self.client.CanvasAuthProvider.account_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def update_authentication_provider(self):

        url = self.base_url + '/api/v1/accounts/{}/authentication_providers/{}'.format(self.client.CanvasAuthProvider.account_id,self.client.CanvasAuthProvider.authentication_provider_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def get_authentication_provider(self):

        url = self.base_url + '/api/v1/accounts/{}/authentication_providers/{}'.format(self.client.CanvasAuthProvider.account_id,self.client.CanvasAuthProvider.authentication_provider_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def delete_authentication_provider(self):

        url = self.base_url + '/api/v1/accounts/{}/authentication_providers/{}'.format(self.client.CanvasAuthProvider.account_id,self.client.CanvasAuthProvider.authentication_provider_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def show_account_auth_settings(self):

        url = self.base_url + '/api/v1/accounts/{}/sso_settings'.format(self.client.CanvasAuthProvider.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def update_account_auth_settings(self):

        url = self.base_url + '/api/v1/accounts/{}/sso_settings'.format(self.client.CanvasAuthProvider.account_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

class CanvasAuth(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def query_by_login(self):

        url = self.base_url + '/api/v1/audit/authentication/logins/{}'.format(self.client.CanvasAuth.login_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAuth.generate_queries())

        pprint(request)

    def query_by_account(self):

        url = self.base_url + '/api/v1/audit/authentication/accounts/{}'.format(self.client.CanvasAuth.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAuth.generate_queries())

        pprint(request)

    def query_by_user(self):

        url = self.base_url + '/api/v1/audit/authentication/users/{}'.format(self.client.CanvasAuth.user_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasAuth.generate_queries())

        pprint(request)

class CanvasBlueprint(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)


    def get_blueprint_info(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def get_associated_course_information(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/associated_courses'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def update_associated_courses(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/update_associations'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def begin_migration_to_push_to_associated_courses(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def set_or_remove_restrictions_on_blueprint_course(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/restrict_item'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def get_unsynced_changes(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/unsynced_changes'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def list_blueprint_migrations(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def show_blueprint_migration(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations/{}'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id,self.client.CanvasBlueprint.migration_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def get_migration_details(self):

        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations/{}/details'.format(self.client.CanvasBlueprint.course_id,self.client.CanvasBlueprint.template_id,self.client.CanvasBlueprint.migration_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)















