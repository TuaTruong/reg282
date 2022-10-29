from binhex import openrsrc
import email
from lib2to3.pgen2 import driver
from re import L
from time import sleep
from webbrowser import Chrome
from selenium import webdriver
import os
import zipfile
import names
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

class Chromedriver:
    def __init__(self,ipForm):
        PROXY_HOST = ipForm.split(":")[0]
        PROXY_PORT =ipForm.split(":")[1]
        PROXY_USER =ipForm.split(":")[2]
        PROXY_PASS = ipForm.split(":")[3]
        PROXY_PORT = int(PROXY_PORT)

        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)



        path = os.path.dirname(os.path.abspath(__file__))
        chrome_options = webdriver.ChromeOptions()

        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
        list_ua = open("ua.txt").read().split("\n")
        chrome_options.add_argument("user-agent="+random.choice(list_ua))
        self.driver = webdriver.Chrome(
            os.path.join(path, 'chromedriver'),
            chrome_options=chrome_options)
        self.driver.set_window_size(480,480)

    def reg282(self):
        name = names.get_full_name().split(" ")
        mail = name[0].lower()+name[1].lower() + str(random.randint(10000000,999999999999999999)) + "@outlook.com"

        self.driver.get("https://www.facebook.com/reg")
        sleep(2)

        try:
            self.driver.find_element("xpath",'//input[@value="Back"]').click()
        except:pass
        self.driver.find_element("name",'firstname').send_keys(name[0])
        self.driver.find_element("name",'lastname').send_keys(name[1])
        self.driver.find_element("name",'reg_email__').send_keys(mail)
        self.driver.find_element("name",'reg_email_confirmation__').send_keys(mail)
        passw = "helloanhem" + str(random.randint(10000000,999999999999999999))
        self.driver.find_element("name",'reg_passwd__').send_keys(passw)

        self.driver.execute_script(f'document.querySelector("#day").value = {random.randint(1,29)}')
        self.driver.execute_script(f'document.querySelector("#month").value = {random.randint(1,10)}')
        self.driver.execute_script(f'document.querySelector("#year").value = {random.randint(1990,2000)}')
        self.driver.find_elements("name", "sex")[random.randint(0,1)].click()

        self.driver.find_element("name","websubmit").click()
        try:
            sleep(5)
            self.driver.execute_script('document.querySelectorAll("span")[8].click()')
            self.driver.quit()
            return mail+"|"+passw
        except:
            self.driver.quit()
            print("fail")
