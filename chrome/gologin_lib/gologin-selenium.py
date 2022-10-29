import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from gologin import getRandomPort


gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzVhMDRmYmY5Y2FjZTE1NThlNWIxOGMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzVhMDUwZDhmNjdlN2I3NGZiOGNkOGYifQ.BHOEimvInQuW2NcIwNyqt6-Kip92JzgSU7X8Y4sD7jE",
	"profile_id": GoLogin.createEmptyProfile()
	})


debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
time.sleep(3)
driver.close()
gl.stop()