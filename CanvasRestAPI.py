import requests

from CanvasClient import CanvasClient
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from pprint import pprint


class OAuthRequests(CanvasClient):

    def __init__(self, client):
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

        url = 'https://{}/login/oauth2/auth?client_id={}&response_type=code&state={}&redirect_uri={}'.format(
            self.install_url, self.client_id, self.state, self.redirect_uri)

        br.get(url)

        ### user accepts, then canvas sends a oauth2 code in the query response


#######################
# API TOKEN SCOPES API
#######################

class CanvasTokenScopes(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_scopes(self):
        url = self.base_url + '/api/v1/accounts/{}/scopes'.format(self.client.CanvasTokenScopes.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasTokenScopes.generate_queries())

        pprint(request)


class CanvasAccountDomainLookup(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def search_account_domains(self):
        url = self.base_url + '/api/v1/accounts/search'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAccountDomainLookup.generate_queries())

        pprint(request)


class CanvasAccountNotifications(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def get_index_of_user_global_notification(self):
        url = self.base_url + '/api/v1/accounts/{}/account_notifications'.format(
            self.client.CanvasAccountNotifications.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAccountNotifications.generate_queries())

        pprint(request)

    def show_global_notification(self):
        url = self.base_url + '/api/v1/accounts/{}/account_notifications/{}'.format(
            self.client.CanvasAccountNotifications.account_id,
            self.client.CanvasAccountNotifications.account_notification_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def close_notification(self):
        url = self.base_url + '/api/v1/accounts/{}/account_notifications/{}'.format(
            self.client.CanvasAccountNotifications.account_id,
            self.client.CanvasAccountNotifications.account_notification_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_global_notification(self):
        url = self.base_url + '/api/v1/accounts/{}/account_notifications'.format(
            self.client.CanvasAccountNotifications.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAccountNotifications.generate_queries())

        pprint(request)

    def update_global_notification(self):
        url = self.base_url + '/api/v1/accounts/{}/account_notifications/{}'.format(
            self.client.CanvasAccountNotifications.account_id,
            self.client.CanvasAccountNotifications.account_notification_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               data=self.client.CanvasAccountNotifications.generate_queries())

        pprint(request)


class CanvasAccountReports(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_available_reports(self):
        url = self.base_url + '/api/v1/accounts/{}/reports'.format(self.client.CanvasAccountReport.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def start_report(self):
        url = self.base_url + '/api/v1/accounts/{}/reports/{}'.format(self.client.CanvasAccountReport.account_id,
                                                                      self.client.CanvasAccountReport.report_type)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAccountReport.generate_queries())

        pprint(request)

    def index_of_reports(self):
        url = self.base_url + '/api/v1/accounts/{}/reports/{}'.format(self.client.CanvasAccountReport.account_id,
                                                                      self.client.CanvasAccountReport.report_type)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def report_status(self):
        url = self.base_url + '/api/v1/accounts/{}/reports/{}/{}'.format(self.client.CanvasAccountReport.account_id,
                                                                         self.client.CanvasAccountReport.report_type,
                                                                         self.client.CanvasAccountReport.report_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def delete_report(self):
        url = self.base_url + '/api/v1/accounts/{}/reports/{}/{}'.format(self.client.CanvasAccountReport.account_id,
                                                                         self.client.CanvasAccountReport.report_type,
                                                                         self.client.CanvasAccountReport.report_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasAccount(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_accounts(self):
        url = self.base_url + '/api/v1/accounts'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def get_admin_manageable_accounts(self):
        url = self.base_url + '/api/v1/manageable_accounts'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_course_admin_accounts(self):
        url = self.base_url + '/api/v1/course_accounts'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_account(self):
        url = self.base_url + '/api/v1/accounts/{}'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_account_settings(self):
        url = self.base_url + '/api/v1/accounts/{}/settings'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_account_permissions(self):
        url = self.base_url + '/api/v1/accounts/{}/permissions'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def get_accounts_sub_accounts(self):
        url = self.base_url + '/api/v1/accounts/{}/sub_accounts'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def get_terms_of_service(self):
        url = self.base_url + '/api/v1/accounts/{}/terms_of_service'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_account_help_links(self):
        url = self.base_url + '/api/v1/accounts/{}/help_links'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_account_active_courses(self):
        url = self.base_url + '/api/v1/accounts/{}/courses'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_account(self):
        url = self.base_url + '/api/v1/accounts/{}'.format(self.client.CanvasAccount.account_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               data=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def delete_root_account_user(self):
        url = self.base_url + '/api/v1/accounts/{}/users/{}'.format(self.client.CanvasAccount.account_id,
                                                                    self.client.CanvasAccount.user_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def create_new_sub_account(self):
        url = self.base_url + '/api/v1/accounts/{}/sub_accounts'.format(self.client.CanvasAccount.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAccount.generate_queries())

        pprint(request)

    def delete_sub_account(self):
        url = self.base_url + '/api/v1/accounts/{}/sub_accounts/{}'.format(self.client.CanvasAccount.account_id,
                                                                           self.client.CanvasAccount.sub_account_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasAccount.generate_queries())

        pprint(request)


class CanvasAdmin(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def make_account_admin(self):
        url = self.base_url + '/api/v1/accounts/{}/admins'.format(self.client.CanvasAdmin.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAdmin.generate_queries())

        pprint(request)

    def remove_account_admin(self):
        url = self.base_url + '/api/v1/accounts/{}/admins/{}'.format(self.client.CanvasAdmin.account_id,
                                                                     self.client.CanvasAdmin.admin_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasAdmin.generate_queries())

        pprint(request)

    def list_account_admins(self):
        url = self.base_url + '/api/v1/accounts/{}/admins'.format(self.client.CanvasAdmin.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAdmin.generate_queries())

        pprint(request)


class CanvasAnalytics(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def get_term_department_level_participation_data(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/terms/{}/activity'.format(
            self.client.CanvasAnalytics.account_id, self.client.CanvasAnalytics.term_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_current_department_level_analytics(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/current/activity'.format(
            self.client.CanvasAnalytics.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_completed_department_level_analytics(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/completed/activity'.format(
            self.client.CanvasAnalytics.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_term_department_grade_data(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/terms/{}/grades'.format(
            self.client.CanvasAnalytics.account_id, self.client.CanvasAnalytics.term_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_current_department_grade_data(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/current/grades'.format(
            self.client.CanvasAnalytics.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_term_department_statistics(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/terms/{}/statistics'.format(
            self.client.CanvasAnalytics.account_id, self.client.CanvasAnalytics.term_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_current_department_statistics(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/current/statistics'.format(
            self.client.CanvasAnalytics.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_completed_department_statistics(self):
        url = self.base_url + '/api/v1/accounts/{}/analytics/completed/statistics'.format(
            self.client.CanvasAnalytics.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_level_participation_data(self):
        url = self.base_url + '/api/v1/courses/{}/analytics/activity'.format(self.client.CanvasAnalytics.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_level_assignment_data(self):
        url = self.base_url + '/api/v1/courses/{}/analytics/assignments'.format(self.client.CanvasAnalytics.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_level_student_summary_data(self):
        url = self.base_url + '/api/v1/courses/{}/analytics/student_summaries'.format(
            self.client.CanvasAnalytics.course_id)

        request = requests.get(url, auth={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAnalytics.generate_queries())

        pprint(request)

    def get_user_participation_data(self):
        url = self.base_url + '/api/v1/courses/{}/analytics/users/{}/activity'.format(
            self.client.CanvasAnalytics.course_id, self.client.CanvasAnalytics.student_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_user_assignment_data(self):
        url = self.base_url + '/api/v1/courses/{}/analytics/users/{}/assignments'.format(
            self.client.CanvasAnalytics.course_id, self.client.CanvasAnalytics.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_user_messaging_data(self):
        url = self.base_url + '/api/v1/courses/{}/analytics/users/{}/communication'.format(
            self.client.CanvasAnalytics.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasExternalFeed(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_external_feed_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/external_feeds'.format(self.client.CanvasExternalFeed.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_external_feed_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/external_feeds'.format(self.client.CanvasExternalFeed.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_external_feed_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/external_feeds'

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)

    def create_external_feed_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/external_feeds'.format(self.client.CanvasExternalFeed.group_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)

    def delete_external_feed_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/external_feeds/{}'.format(self.client.CanvasExternalFeed.course_id,
                                                                            self.client.CanvasExternalFeed.external_feed_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)

    def delete_external_feed_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/external_feeds/{}'.format(self.client.CanvasExternalFeed.group_id,
                                                                           self.client.CanvasExternalFeed.external_feed_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasExternalFeed.generate_queries())

        pprint(request)


class CanvasAnnouncement(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_announcements(self):
        url = self.base_url + '/api/v1/announcements'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAnnouncements.generate_queries())

        pprint(request)


class CanvasAppointmentGroups(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_appointment_groups(self):
        url = self.base_url + '/api/v1/appointment_groups'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def create_appointment_group(self):
        url = self.base_url + '/api/v1/appointment_groups'

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def get_single_appointment_group(self):
        url = self.base_url + '/api/v1/appointment_groups/{}'.format(
            self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def update_appointment_group(self):
        url = self.base_url + '/api/v1/appointment_groups/{}'.format(
            self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               data=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def delete_appointment_group(self):
        url = self.base_url + '/api/v1/appointment_groups/{}'.format(
            self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def list_user_participants(self):
        url = self.base_url + '/api/v1/appointment_groups/{}/users'.format(
            self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def list_student_group_participants(self):
        url = self.base_url + '/api/v1/appointment_groups/{}/groups'.format(
            self.client.CanvasAppointmentGroup.appointment_group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)

    def get_next_appointment(self):
        url = self.base_url + '/api/v1/appointment_groups/next_appointment'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAppointmentGroup.generate_queries())

        pprint(request)


class CanvasAssignmentExtensions(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def set_extensions_student_assignment_submissions(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}/extensions'.format(
            self.client.CanvasAssignmentExtensions.course_id, self.client.CanvasAssignmentExtensions.assignment_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAssignmentExtensions.generate_queries())

        pprint(request)


class CanvasAssignmentGroups(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_assignment_groups(self):
        url = self.base_url + "/api/v1/courses/{}/assignment_groups".format(
            self.client.CanvasAssignmentGroups.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.client.CanvasAssignmentGroups.course_id)},
                               data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def get_assignment_group(self):
        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}'.format(
            self.client.CanvasAssignmentGroups.course_id, self.client.CanvasAssignmentGroups.assignment_group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def create_assignment_group(self):
        url = self.base_url + '/api/v1/courses/{}/assignment_groups'.format(
            self.client.CanvasAssignmentGroups.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def edit_assignment_group(self):
        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}'.format(
            self.client.CanvasAssignmentGroups.course_id, self.client.CanvasAssignmentGroups.assignment_group_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)

    def destroy_assignment_group(self):
        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}'.format(
            self.client.CanvasAssignmentGroups.course_id, self.client.CanvasAssignmentGroups.assignment_group_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  data=self.client.CanvasAssignmentGroups.generate_queries())

        pprint(request)


class CanvasAssignments(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def delete_assignment(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}'.format(self.client.CanvasAssignments.course_id,
                                                                         self.client.CanvasAssignments.assignment_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_assignments_v1(self):
        url = self.base_url + '/api/v1/courses/{}/assignments'.format(self.client.CanvasAssignments.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def list_assignments_v2(self):
        url = self.base_url + '/api/v1/courses/{}/assignment_groups/{}/assignments'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def list_user_assignments(self):
        url = self.base_url + '/api/v1/users/{}/courses/{}/assignments'.format(self.client.CanvasAssignments.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def duplicate_assignment(self):
        url = self.base_url + '/api/v1/courses/{}/assingments/{}/duplicate'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def get_single_assignment(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}'.format(self.client.CanvasAssignments.course_id,
                                                                         self.client.CanvasAssignments.assignment_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def create_assignment(self):
        url = self.base_url + '/api/v1/courses/{}/assignments'.format(self.client.CanvasAssignments.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def edit_assignment(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}'.format(self.client.CanvasAssignments.course_id,
                                                                         self.client.CanvasAssignments.assignment_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def bulk_update_dates(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/bulk_update'.format(
            self.client.CanvasAssignments.course_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def list_assignment_overrides(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_assignment_override(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides/{}'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id,
            self.client.CanvasAssignments.override_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def redirect_assignment_override_to_group(self):
        url = self.base_url + '/api/v1/groups/{}/assignments/{}/override'.format(self.client.CanvasAssignments.group_id,
                                                                                 self.client.CanvasAssignments.assignment_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def redirect_assignment_override_to_section(self):
        url = self.base_url + '/api/v1/sections/{}/assignments/{}/override'.format(
            self.client.CanvasAssignments.course_section_id, self.client.CanvasAssignments.assignment_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_assignment_override(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def update_assignment_override(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides/{}'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id,
            self.client.CanvasAssignments.override_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def delete_assignment_override(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/{}/overrides/{}'.format(
            self.client.CanvasAssignments.course_id, self.client.CanvasAssignments.assignment_id,
            self.client.CanvasAssignments.override_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def batch_retrieve_overrides_in_course(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/overrides'.format(self.client.CanvasAssignments.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def batch_create_overrides_in_course(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/overrides'.format(self.client.CanvasAssignments.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasAssignments.generate_queries())

        pprint(request)

    def batch_update_overrides_in_course(self):
        url = self.base_url + '/api/v1/courses/{}/assignments/overrides'.format(self.client.CanvasAssignments.course_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAssignments.generate_queries())

        pprint(request)


class CanvasAuthenticationProviders(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_authentication_providers(self):
        url = self.base_url + '/api/v1/accounts/{}/authentication_providers'.format(
            self.client.CanvasAuthProvider.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def add_authentication_provider(self):
        url = self.base_url + '/api/v1/accounts/{}/authentication_providers'.format(
            self.client.CanvasAuthProvider.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def update_authentication_provider(self):
        url = self.base_url + '/api/v1/accounts/{}/authentication_providers/{}'.format(
            self.client.CanvasAuthProvider.account_id, self.client.CanvasAuthProvider.authentication_provider_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def get_authentication_provider(self):
        url = self.base_url + '/api/v1/accounts/{}/authentication_providers/{}'.format(
            self.client.CanvasAuthProvider.account_id, self.client.CanvasAuthProvider.authentication_provider_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def delete_authentication_provider(self):
        url = self.base_url + '/api/v1/accounts/{}/authentication_providers/{}'.format(
            self.client.CanvasAuthProvider.account_id, self.client.CanvasAuthProvider.authentication_provider_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def show_account_auth_settings(self):
        url = self.base_url + '/api/v1/accounts/{}/sso_settings'.format(self.client.CanvasAuthProvider.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)

    def update_account_auth_settings(self):
        url = self.base_url + '/api/v1/accounts/{}/sso_settings'.format(self.client.CanvasAuthProvider.account_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasAuthProvider.generate_queries())

        pprint(request)


class CanvasAuth(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def query_by_login(self):
        url = self.base_url + '/api/v1/audit/authentication/logins/{}'.format(self.client.CanvasAuth.login_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAuth.generate_queries())

        pprint(request)

    def query_by_account(self):
        url = self.base_url + '/api/v1/audit/authentication/accounts/{}'.format(self.client.CanvasAuth.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAuth.generate_queries())

        pprint(request)

    def query_by_user(self):
        url = self.base_url + '/api/v1/audit/authentication/users/{}'.format(self.client.CanvasAuth.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasAuth.generate_queries())

        pprint(request)


class CanvasBlueprint(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def get_blueprint_info(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}'.format(self.client.CanvasBlueprint.course_id,
                                                                                 self.client.CanvasBlueprint.template_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_associated_course_information(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/associated_courses'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_associated_courses(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/update_associations'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def begin_migration_to_push_to_associated_courses(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def set_or_remove_restrictions_on_blueprint_course(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/restrict_item'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasBlueprint.generate_queries())

        pprint(request)

    def get_unsynced_changes(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/unsynced_changes'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_blueprint_migrations(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def show_blueprint_migration(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations/{}'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id,
            self.client.CanvasBlueprint.migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_migration_details(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_templates/{}/migrations/{}/details'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.template_id,
            self.client.CanvasBlueprint.migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_blueprint_subscriptions(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_subscriptions'.format(self.client.CanvasBlueprint.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_blueprint_imports(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_subscriptions/{}/migrations'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.subscription_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def show_blueprint_import(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_subscriptions/{}/migrations/{}'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.subscription_id,
            self.client.CanvasBlueprint.migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_import_details(self):
        url = self.base_url + '/api/v1/courses/{}/blueprint_subscriptions/{}/migrations/{}/details'.format(
            self.client.CanvasBlueprint.course_id, self.client.CanvasBlueprint.subscription_id,
            self.client.CanvasBlueprint.migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasBookmarks(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_bookmarks(self):
        url = self.base_url + '/api/v1/users/self/bookmarks'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_bookmark(self):
        url = self.base_url + '/api/v1/users/self/bookmarks'

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasBookmark.generate_queries())

        pprint(request)

    def get_bookmark(self):
        url = self.base_url + '/api/v1/users/self/bookmarks/{}'.format(self.client.CanvasBookmark.bookmark_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasBookmark.generate_queries())

        pprint(request)

    def update_bookmark(self):
        url = self.base_url + '/api/v1/users/self/bookmarks/{}'.format(self.client.CanvasBookmark.bookmark_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasBookmark.generate_queries())

        pprint(request)

    def delete_bookmark(self):
        url = self.base_url + '/api/v1/users/self/bookmarks/{}'.format(self.client.CanvasBookmark.bookmark_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasBrandConfigurations(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def get_brand_config_variables(self):
        url = self.base_url + '/api/v1/brand_variables/'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasCalendarEvents(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_calendar_events(self):
        url = self.base_url + '/api/v1/calendar_events'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def list_user_calendar_events(self):
        url = self.base_url + '/api/v1/users/{}/calendar_events'.format(self.client.CanvasCalendarEvents.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def create_calendar_event(self):
        url = self.base_url + '/api/v1/calendar_events'

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def get_single_calendar_event(self):
        url = self.base_url + '/api/v1/calendar_events/{}'.format(self.client.CanvasCalendarEvents.calendar_event_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def reverse_time_slot(self):
        url = self.base_url + '/api/v1/calendar_events/{}/reservations'.format(
            self.client.CanvasCalendarEvents.calendar_event_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def reverse_time_slot_participant_id(self):
        url = self.base_url + '/api/v1/calendar_events/{}/reservations/{}'.format(
            self.client.CanvasCalendarEvents.calendar_event_id, self.client.CanvasCalendarEvents.participant_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def update_calendar_event(self):
        url = self.base_url + '/api/v1/calendar_events/{}'.format(self.client.CanvasCalendarEvents.calendar_event_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def delete_calendar_event(self):
        url = self.base_url + '/api/v1/calendar_events/{}'.format(self.client.CanvasCalendarEvents.calendar_event_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def set_course_timetable(self):
        url = self.base_url + '/api/v1/courses/{}/calendar_events/timetable'.format(
            self.client.CanvasCalendarEvents.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)

    def get_course_timetable(self):
        url = self.base_url + '/api/v1/courses/{}/calendar_events/timetable'.format(
            self.client.CanvasCalendarEvents.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_or_update_timetable_events_directly(self):
        url = self.base_url + '/api/v1/courses/{}/calendar_events/timetable_events'.format(
            self.client.CanvasCalendarEvents.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasCalendarEvents.generate_queries())

        pprint(request)


class CanvasCollaborations(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_collaborations_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/collaborations'.format(self.client.CanvasCollaboration.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_collaborations_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/collaborations'.format(self.client.CanvasCollaboration.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_collaboration_members(self):
        url = self.base_url + '/api/v1/collaborations/{}/members'.format(
            self.client.CanvasCollaboration.collaboration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasCollaboration.generate_queries())

        pprint(request)

    def list_potential_members(self):
        url = self.base_url + '/api/v1/courses/{}/potential_collaborators'.format(
            self.client.CanvasCollaboration.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_potential_members_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/potential_collaborators'.format(
            self.client.CanvasCollaboration.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasCommunicationMessages(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_comm_messages_for_user(self):
        url = self.base_url + '/api/v1/comm_messages'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasCommMessages.generate_queries())

        pprint(request)

    def create_communication_channel(self):
        url = self.base_url + '/api/v1/users/{}/communication_channels'.format(self.client.CanvasCommMessages.user_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasCommMessages.generate_queries())

        pprint(request)

    def delete_communication_channel_v1(self):
        url = self.base_url + '/api/v1/users/{}/communication_channels/{}'.format(
            self.client.CanvasCommMessages.user_id, self.client.CanvasCommMessages.communication_channel_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  json=self.client.CanvasCommMessages.generate_queries())

        pprint(request)

    def delete_communication_channel_v2(self):
        url = self.base_url + '/api/v1/users/{}/communication_channels/{}/{}'.format(
            self.client.CanvasCommMessages.user_id, self.client.CanvasCommMessages.communication_channel_type,
            self.client.CanvasCommMessages.communication_channel_address)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)},
                                  json=self.client.CanvasCommMessages.generate_queries())

        pprint(request)

    def delete_push_notification_endpoint(self):
        url = self.base_url + '/api/v1/users/self/communication_channels/push'

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasConference(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_conferences_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/conferences'.format(self.client.CanvasConferences.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_conferences_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/conferences'.format(self.client.CanvasConferences.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_conferences_current_user(self):
        url = self.base_url + '/api/v1/conferences'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasContentExport(CanvasClient):

    def __init__(self, client):
        self.base_url = 'https://{}'.format(self.install_url)
        self.client = client

    def list_content_exports_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_exports'.format(self.client.CanvasContentExports.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_exports_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_exports'.format(self.client.CanvasContentExports.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_exports_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_exports'.format(self.client.CanvasContentExports.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def show_content_export_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_exports/{}'.format(self.client.CanvasContentExports.course_id,
                                                                             self.client.CanvasContentExports.content_export_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def show_content_export_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_exports/{}'.format(self.client.CanvasContentExports.group_id,
                                                                            self.client.CanvasContentExports.content_export_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def show_content_export_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_exports/{}'.format(self.client.CanvasContentExports.user_id,
                                                                           self.client.CanvasContentExports.content_export_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def export_content_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_exports'.formt(self.client.CanvasContentExports.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentExports.generate_queries())

        pprint(request)

    def export_content_group_id(self):
        url = self.base_url = '/api/v1/groups/{}/content_exports'.format(self.client.CanvasContentExports.group_id)

        request = requests.post(url, headers={'Authorization {}'.fomrat(self.token)},
                                json=self.client.CanvasContentExports.generate_queries())

        pprint(request)

    def export_content_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_exports'.format(self.client.CanvasContentExports.user_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentExports.generate_queries())

        pprint(request)


class CanvasContentMigration(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_migration_issues_acocunt_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}/migration_issues'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_issues_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}/migration_issues'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_issues_group_id(self):
        url = self.base_url = '/api/v1/groups/{}/content_migrations/{}/migration_issues'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_issues_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}/migration_issues'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_migration_issue_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_migration_issue_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_migration_issue_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_migration_issue_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_migration_issue_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_migration_issue_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_migration_issue_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_migration_issue_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}/migration_issues/{}'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id,
            self.client.CanvasContentMigration.migration_issue_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def list_content_migrations_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations'.format(
            self.client.CanvasContentMigration.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_migrations_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations'.format(
            self.client.CanvasContentMigration.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_migrations_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations'.format(self.client.CanvasContentMigration.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_migrations_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations'.format(self.client.CanvasContentMigration.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_content_migration_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations'.format(
            self.client.CanvasContentMigration.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def create_content_migration_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations'.format(
            self.client.CanvasContentMigration.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def create_content_migration_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations'.format(self.client.CanvasContentMigration.user_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_content_migration_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_content_migration_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_content_migration_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_content_migration_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def list_content_migrations_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations'.format(
            self.client.CanvasContentMigration.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_migrations_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations'.format(
            self.client.CanvasContentMigration.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_migrations_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations'.format(self.client.CanvasContentMigration.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_migrations_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations'.format(self.client.CanvasContentMigration.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_migration_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_content_migration_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations'.format(
            self.client.CanvasContentMigration.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def create_content_migration_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations'.format(
            self.client.CanvasContentMigration.course_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def create_content_migration_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations'.format(self.client.CanvasContentMigration.group_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def create_content_migration_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations'.format(self.client.CanvasContentMigration.user_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def update_content_migration_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_content_migration_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_content_migration_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_content_migration_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_system_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/migrators'.format(
            self.client.CanvasContentMigration.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_system_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/migrators'.format(
            self.client.CanvasContentMigration.course_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_system_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/migrators'.format(
            self.client.CanvasContentMigration.group_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_migration_system_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/migrators'.format(
            self.client.CanvasContentMigration.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_items_for_selective_import_account_id(self):
        url = self.base_url + '/api/v1/accounts/{}/content_migrations/{}/selective_data'.format(
            self.client.CanvasContentMigration.account_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def list_items_for_selective_import_course_id(self):
        url = self.base_url + '/api/v1/courses/{}/content_migrations/{}/selective_data'.format(
            self.client.CanvasContentMigration.course_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def list_items_for_selective_import_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/content_migrations/{}/selective_data'.format(
            self.client.CanvasContentMigration.group_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasContentMigration.generate_queries())

        pprint(request)

    def list_items_for_selective_import_user_id(self):
        url = self.base_url + '/api/v1/users/{}/content_migrations/{}/selective_data'.format(
            self.client.CanvasContentMigration.user_id, self.client.CanvasContentMigration.content_migration_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasContentMigration.generate_queries())

        pprint(request)


class CanvasContentSecurity(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def get_current_settings_for_account(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_settings'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_current_settings_for_course(self):
        url = self.base_url + '/api/v1/courses/{}/csp_settings'.format(
            self.client.CanvasContentSecurityPolicySettings.course_id)

        request = requests.get(url, headers={'Authorization'.format(self.token)})

        pprint(request)

    def enable_or_disable_or_clear_csp_setting_for_course(self):
        url = self.base_url + '/api/v1/courses/{}/csp_settings'.format(
            self.client.CanvasContentSecurityPolicySettings.course_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def enable_or_disable_or_clear_csp_setting_for_account(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_settings'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def lock_or_unlock_csp_setting_account_and_courses(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_settings/lock'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasContentSecurityPolicySettings.generate_queries())

        pprint(request)

    def add_allowed_domain_to_account(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_settings/domains'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentSecurityPolicySettings.generate_queries())

        pprint(request)

    def add_multiple_domains_to_account(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_settings/domains/batch_create'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentSecurityPolicySettings.generate_queries())

        pprint(request)

    def retrieve_reported_csp_violations_for_account(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_log'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def remove_domain_from_account(self):
        url = self.base_url + '/api/v1/accounts/{}/csp_settings/domains'.format(
            self.client.CanvasContentSecurityPolicySettings.account_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


class CanvasContentShare(CanvasClient):

    def __init__(self, client):
        self.base_url + 'https://{}'.format(self.install_url)
        self.client = client

    def create_content_share(self):
        url = self.base_url + '/api/v1/users/{}/content_shares'.format(self.client.CanvasContentShares.user_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasContentShares.generate_queries())

        pprint(request)

    def list_content_shares_sent(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/sent'.format(self.client.CanvasContentShares.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_content_shares_received(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/received'.format(self.client.CanvasContentShares.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_unread_shares_count(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/unread_count'.format(
            self.client.CanvasContentShares.user_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_content_share(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/{}'.format(self.client.CanvasContentShares.user_id,
                                                                          self.client.CanvasContentShares.content_export_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def remove_content_share(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/{}'.format(self.client.CanvasContentShares.user_id,
                                                                          self.client.CanvasContentShares.content_export_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def add_user_to_content_share(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/{}/add_users'.format(
            self.client.CanvasContentShares.user_id, self.client.CanvasContentShares.content_share_id)

        request = requests.post(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_content_share(self):
        url = self.base_url + '/api/v1/users/{}/content_shares/{}'.format(self.client.CanvasContentShares.user_id,
                                                                          self.client.CanvasContentShares.content_share_id)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasContentShares.generate_queries())

        pprint(request)


class CanvasConversations(CanvasClient):

    def __init__(self, client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_conversations(self):
        url = self.base_url + '/api/v1/conversations'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def create_conversation(self):
        url = self.base_url + '/api/v1/conversations'

        request = requests.post(url, headers={'Authorization {}'.format(self.token)},
                                json=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def get_running_batches(self):
        url = self.base_url + '/api/v1/conversations/batches'

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_conversation(self):
        url = self.base_url + '/api/v1/conversations/{}'.format(self.client.CanvasConversations.conversation_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)},
                               params=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def edit_conversation(self):
        url = self.base_url + '/api/v1/conversations/{}'.format(self.token)

        request = requests.put(url, headers={'Authorization {}'.format(self.token)},
                               json=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def mark_all_as_read(self):
        url = self.base_url + '/api/v1/conversations/mark_all_as_read'

        request = requests.post(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def delete_conversation(self):
        url = self.base_url + '/api/v1/conversations/{}'.format(self.client.CanvasConversations.conversation_id)

        request = requests.delete(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def add_recipients(self):

        url = self.base_url + '/api/v1/conversations/{}/add_recipients'.format(self.client.CanvasConversations.conversation_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def add_message(self):

        url = self.base_url + '/api/v1/conversations/{}/add_message'.format(self.client.CanvasConversations.conversation_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def delete_message(self):

        url = self.base_url + '/api/v1/conversations/{}/remove_messages'.foramt(self.client.CanvasConversations.conversation_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def batch_update_conversations(self):

        url = self.base_url + '/api/v1/conversations'

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasConversations.generate_queries())

        pprint(request)

    def find_recipients(self):

        url = self.base_url + '/api/v1/conversations/find_recipients'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def unread_count(self):

        url = self.base_url + '/api/v1/conversations/unread_count'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

class CanvasCourseAuditLog(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def query_by_account(self):

        url = self.base_url + '/api/v1/audit/course/accounts/{}'.format(self.client.CanvasAccount.account_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourseAuditLog.account_id)

        pprint(request)

    def query_by_course(self):

        url = self.base_url + '/api/v1/audit/course/courses/{}'.format(self.client.CanvasCourseAuditLog.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourseAuditLog.generate_queries())

        pprint(request)

class CanvasCourseQuizExtensions(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def set_extensions_for_student_quiz_submissions(self):

        url = self.base_url + '/api/v1/courses/{}/quiz_extensions'.format(self.client.CanvasCourseQuizExtensions.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCourseQuizExtensions.generate_queries())

        pprint(request)

class CanvasCourses(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_courses(self):

        url = self.base_url + '/api/v1/courses'

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def list_courses_for_user(self):

        url = self.base_url + '/api/v1/users/{}/courses'.format(self.client.CanvasCourses.user_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def get_user_progress(self):

        url = self.base_url + '/api/v1/courses/{}/users/{}/progress/'.format(self.client.CanvasCourses().course_id,self.client.CanvasCourses.user_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def create_new_course(self):

        url = self.base_url + '/api/v1/accounts/{}/courses'.format(self.client.CanvasCourses.account_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def upload_file(self):

        url = self.base_url + '/api/v1/courses/{}/files'.format(self.client.CanvasCourses.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_students(self):

        url = self.base_url + '/api/v1/courses/{}/students'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_users_in_course(self):

        url = self.base_url + '/api/v1/courses/{}/users'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def list_users_in_course_searched_users(self):

        url = self.base_url + '/api/v1/courses/{}/search_users'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def list_recently_logged_students(self):

        url = self.base_url + '/api/v1/courses/{}/recent_students'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_user(self):

        url = self.base_url + '/api/v1/courses/{}/users/{}'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def search_for_content_share_users(self):

        url = self.base_url + '/api/v1/courses/{}/content_share_users'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def preview_processed_html(self):

        url = self.base_url + '/api/v1/courses/{}/preview_html'.format(self.client.CanvasCourses.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def get_course_activity_stream(self):

        url = self.base_url + '/api/v1/courses/{}/activity_stream'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_activity_stream_summary(self):

        url = self.base_url + '/api/v1/courses/{}/activity_stream/summary'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_todo_items(self):

        url = self.base_url + '/api/v1/courses/{}/todo'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def delete_conclude_course(self):

        url = self.base_url + '/api/v1/courses/{}'.format(self.client.CanvasCourses.course_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCourses().generate_queries())

        pprint(request)

    def get_course_settings(self):

        url = self.base_url + '/api/v1/courses/{}/settings'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def update_course_settings(self):

        url = self.base_url + '/api/v1/courses/{}/settings'.format(self.client.CanvasCourses.course_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def return_test_student(self):

        url = self.base_url + '/api/v1/courses/{}/student_view_student'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_course_course_id(self):

        url = self.base_url + '/api/v1/courses/{}'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def get_single_course_account_id(self):

        url = self.base_url + '/api/v1/accounts/{}/courses/{}'.format(self.client.CanvasCourses.account_id,self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def update_course(self):

        url = self.base_url + '/api/v1/courses/{}'.format(self.client.CanvasCourses.course_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def update_courses(self):

        url = self.base_url + '/api/v1/account/{}/courses'.format(self.client.CanvasCourses.account_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def reset_course(self):

        url = self.base_url + '/api/v1/courses/{}/reset_content'.format(self.client.CanvasCourses.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_effective_due_dates(self):

        url = self.base_url + '/api/v1/courses/{}/effective_due_dates'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCourses.generate_queries())

        pprint(request)

    def get_course_permissions(self):

        url = self.base_url + '/api/v1/courses/{}/permissions'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_bulk_user_progress(self):

        url = self.base_url + '/api/v1/courses/{}/bulk_user_progress'.format(self.client.CanvasCourses.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_course_copy_status(self):

        url = self.base_url + '/api/v1/courses/{}/course_copy/{}'.format(self.client.CanvasCourses.course_id,self.client.CanvasCourses.course_copy_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def copy_course_content(self):

        url = self.base_url + '/api/v1/courses/{}/course_copy'.format(self.client.CanvasCourses.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

class CanvasCustomGradebook(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_custom_gradebook_columns(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_columns'.format(self.client.CanvasCustomGradebook.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCustomGradebook.generate_queries())

        pprint(request)

    def create_custom_gradebook_column(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_columns'.format(self.client.CanvasCustomGradebook.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCustomGradebook.generate_queries())

        pprint(request)

    def update_custom_gradebook_column(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_columns/{}'.format(self.client.CanvasCustomGradebook.course_id,self.client.CanvasCustomGradebook.custom_gradebook_column_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCustomGradebook.generate_queries())

        pprint(request)

    def delete_custom_gradebook_column(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_columns/{}'.format(self.client.CanvasCustomGradebook.course_id,self.client.CanvasCustomGradebook.custom_gradebook_column_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def reorder_custom_columns(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_columns/reorder'.format(self.client.CanvasCustomGradebook.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCustomGradebook.generate_queries())

        pprint(request)

    def list_entries_for_column(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_columns/{}/data'.format(self.client.CanvasCustomGradebook.course_id,self.client.CanvasCustomGradebook.custom_gradebook_column_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasCustomGradebook.generate_queries())

        pprint(request)

    def update_column_data(self):

        url = self.base_url + '/api/v1/courses/{}/custom_gradebook_column_data'.format(self.client.CanvasCustomGradebook.course_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasCustomGradebook.generate_queries())

        pprint(request)

class CanvasDiscussionTopic(CanvasClient):

    def __init__(self,client):
        self.client = client
        self.base_url = 'https://{}'.format(self.install_url)

    def list_discussion_topics_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics'.format(self.client.CanvasDiscussionTopics.course_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def list_discussion_topics_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics'.format(self.client.CanvasDiscussionTopics.group_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def create_new_discussion_topic_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics'.format(self.client.CanvasDiscussionTopics.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def create_new_dicussion_topic_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics'.format(self.client.CanvasDiscussionTopics.group_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def update_topic_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def update_topic_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def delete_topic_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def delete_topic_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def reorder_pinned_topics_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/reorder'.format(self.client.CanvasDiscussionTopics.course_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def reorder_pinned_topics_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/reorder'.format(self.client.CanvasDiscussionTopics.group_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def update_entry_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries/{}'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id,self.client.CanvasDiscussionTopics.entry_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def update_entry_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries/{}'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id,self.client.CanvasDiscussionTopics.entry_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def delete_entry_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries/{}'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id,self.client.CanvasDiscussionTopics.entry_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def delete_entry_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries/{}'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id,self.client.CanvasDiscussionTopics.entry_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_single_topic_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def get_single_topic_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def get_full_topic_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/view'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def get_full_topic_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/view'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def post_entry_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def post_entry_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def duplicate_discussion_topic_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/duplicate'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def duplicate_discussion_topic_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/duplicate'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.post(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_topic_entries_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_topic_entries_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries'.format(
            self.client.CanvasDiscussionTopics.group_id, self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def post_reply_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries/{}/replies'.format(

            self.client.CanvasDiscussionTopics.course_id,
            self.client.CanvasDiscussionTopics.discussion_topic_id,
            self.client.CanvasDiscussionTopics.entry_id

        )

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def post_reply_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries/{}/replies'.format(

            self.client.CanvasDiscussionTopics.group_id,
            self.client.CanvasDiscussionTopics.discussion_topic_id,
            self.client.CanvasDiscussionTopics.entry_id

        )

        request = requests.post(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def list_entry_reply_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries/{}/replies'.format(

            self.client.CanvasDiscussionTopics.course_id,
            self.client.CanvasDiscussionTopics.discussion_topic_id,
            self.client.CanvasDiscussionTopics.entry_id
        )

        request = requests.get(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def list_entry_reply_group_id(self):
        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries/{}/replies'.format(

            self.client.CanvasDiscussionTopics.course_id,
            self.client.CanvasDiscussionTopics.discussion_topic_id,
            self.client.CanvasDiscussionTopics.entry_id
        )

        request = requests.get(url, headers={'Authorization {}'.format(self.token)})

        pprint(request)


    def list_entries_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entry_list'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def list_entries_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entry_list'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.get(url,headers={'Authorization {}'.format(self.token)},params=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def mark_topic_as_read_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/read'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def mark_topic_as_read_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/read'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def mark_topic_as_unread_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/read'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def mark_topic_as_unread_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/read'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)})

        pprint(request)

    def mark_all_entries_as_read_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/read_all'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def mark_all_entries_as_read_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/read_all'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def mark_all_entries_as_unread(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/read_all'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def mark_all_entries_as_unread_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/read_all'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id)

        request = requests.delete(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

    def mark_entry_as_read_course_id(self):

        url = self.base_url + '/api/v1/courses/{}/discussion_topics/{}/entries/{}/read'.format(self.client.CanvasDiscussionTopics.course_id,self.client.CanvasDiscussionTopics.discussion_topic_id,self.client.CanvasDiscussionTopics.entry_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

    def mark_entry_as_read_group_id(self):

        url = self.base_url + '/api/v1/groups/{}/discussion_topics/{}/entries/{}/read'.format(self.client.CanvasDiscussionTopics.group_id,self.client.CanvasDiscussionTopics.discussion_topic_id,self.client.CanvasDiscussionTopics.entry_id)

        request = requests.put(url,headers={'Authorization {}'.format(self.token)},json=self.client.CanvasDiscussionTopics.generate_queries())

        pprint(request)

