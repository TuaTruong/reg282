from asyncore import read
from weakref import proxy
from selenium import webdriver
import threading
import random
import names
import string
from time import sleep
list_mail = open('mail.txt').read().split("\n")
mail = list_mail[3].split("|")[0]
password = list_mail[3].split("|")[1]
name = names.get_full_name().split(" ")

options = webdriver.ChromeOptions()
proxy = "139.99.82.10:51790"
options.add_argument('--proxy-server=socks5://' + proxy)
ua = open("ua.txt").read().split("\n")[random.randint(0,600)]
options.add_argument(f"user-agent={ua}")
driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com/reg")
driver.find_element("name",'firstname').send_keys(name[0])
driver.find_element("name",'lastname').send_keys(name[1])
driver.find_element("name",'reg_email__').send_keys(mail)
driver.find_element("name",'reg_email_confirmation__').send_keys(mail)
driver.find_element("name",'reg_passwd__').send_keys(password)

driver.execute_script(f'document.querySelector("#day").value = {random.randint(1,29)}')
driver.execute_script(f'document.querySelector("#month").value = {random.randint(1,10)}')
driver.execute_script(f'document.querySelector("#year").value = {random.randint(1990,2000)}')
driver.find_elements("name", "sex")[random.randint(0,1)].click()

driver.find_element("name","websubmit").click()