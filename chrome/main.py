from concurrent.futures import thread
import threading
from webbrowser import Chrome
import ChromeDriver
import random
import time
lock = threading.Lock()
listIp = open("ip.txt").read().split("\n")

def start():
    driver = ChromeDriver.Chromedriver(random.choice(listIp))
    kq = driver.reg282()
    lock.acquire()
    open("success.txt","a").write(kq+"\n")
    lock.release()

# while True:
for i in range(3):
    threading.Thread(target=start).start()
    time.sleep(1)

