from concurrent.futures import thread
import threading
import time
import os
from multiprocessing import Pool
from sys import platform
from matplotlib.pyplot import sca
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin_lib.gologin import GoLogin

def scrap(profile,x):
	gl = GoLogin({
	        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmNiMThmYjA5MjQxMWFiZWUxNWQ3ZjkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MmNiMTk1NDA5MjQxMTdlYzYxNWQ4NDAifQ.9esN3JwcqYrl8VGFFEZYP0yfNav_kS-q9PB_R4qvOaE',
	        'profile_id': profile[x]['profile_id'],
	        'port': profile[x]['port'],
		})

	if platform == "linux" or platform == "linux2":
		chrome_driver_path = './chromedriver'
	elif platform == "darwin":
		chrome_driver_path = './mac/chromedriver'
	elif platform == "win32":
		chrome_driver_path = 'chromedriver.exe'

	debugger_address = gl.start()
	chrome_options = Options()
	chrome_options.add_experimental_option("debuggerAddress", debugger_address)
	driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
	driver.get("http://www.python.org")
	print('ready', profile['profile_id'], driver.title)
	time.sleep(10)
	print('closing', profile['profile_id'])
	driver.close()
	gl.stop()

profiles = [
	{'profile_id': '62cbca9242f1fd4285178176', 'port': 3500}, 
	{'profile_id': '62cbbba2a30773560434b0e9', 'port': 3501},
	{'profile_id': '62cb1ee169a864777f67314f', 'port': 3502},
	]


for i in range(3):
	threading.Thread(target=scrap, args={i,}).start()


if platform == "win32":
	os.system('taskkill /im chrome.exe /f')
	os.system('taskkill /im chromedriver.exe /f')
else:
	os.system('killall -9 chrome')
	os.system('killall -9 chromedriver')
