from time import sleep
from selenium import webdriver
from gologin_lib.gologin import GoLogin
import random
from random import randint
from selenium.webdriver.chrome.options import Options
import names


def create_gologin_profile(token, proxy):
    host,port,username,password = proxy.split(":")
    gl = GoLogin({
        "token": token
    })

    profile_id = gl.create({
        "name": f'{randint(100000000,999999999999999999999)}',
        "os": 'win',
        "navigator": {
            "language": 'enUS',
            "userAgent": "random", 
            "resolution": '480x480',
            "platform": 'win',
        },
        'proxyEnabled': True, # Specify 'false' if not using proxy
        'proxy': {
            'mode': 'http',
            "host":host,
            "port":port,
            "username": username,
            "password": password,
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
            
        },
    })

    #         else: # Create profile with proxy
    # print("Profile_id: ",profile_id)
    return profile_id


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzVhMDRmYmY5Y2FjZTE1NThlNWIxOGMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzVhMDUwZDhmNjdlN2I3NGZiOGNkOGYifQ.BHOEimvInQuW2NcIwNyqt6-Kip92JzgSU7X8Y4sD7jE"
profile_id = create_gologin_profile(token, "202.182.117.108:39974:lazyguys689:loveblue0810")
gl = GoLogin({
    "token": token,
    "profile_id": profile_id,
    "port": random.randint(1000,30000)
    })


debugger_address = gl.start()
chrome_options = Options()
args = ["hide_console", ]
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path="gologin_lib\\chromedriver.exe", options=chrome_options, service_args=args)
driver.set_window_size(480,480)


name = names.get_full_name().split(" ")
mail = name[0].lower()+name[1].lower() + str(random.randint(10000000,999999999999999999)) + "@outlook.com"

driver.get("https://www.facebook.com/reg")
sleep(2)

try:
    driver.find_element("xpath",'//input[@value="Back"]').click()
except:pass
driver.find_element("name",'firstname').send_keys(name[0])
driver.find_element("name",'lastname').send_keys(name[1])
driver.find_element("name",'reg_email__').send_keys(mail)
driver.find_element("name",'reg_email_confirmation__').send_keys(mail)
passw = "helloanhem" + str(random.randint(10000000,999999999999999999))
driver.find_element("name",'reg_passwd__').send_keys(passw)

driver.execute_script(f'document.querySelector("#day").value = {random.randint(1,29)}')
driver.execute_script(f'document.querySelector("#month").value = {random.randint(1,10)}')
driver.execute_script(f'document.querySelector("#year").value = {random.randint(1990,2000)}')
driver.find_elements("name", "sex")[random.randint(0,1)].click()

driver.find_element("name","websubmit").click()
try:
    sleep(5)
    driver.execute_script('document.querySelectorAll("span")[8].click()')
    driver.quit()
    open("success.txt","a").write(mail+"|"+passw + "\n")
except:
    driver.quit()
    print("fail")