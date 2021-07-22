from CanvasClient import CanvasClient
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver


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
