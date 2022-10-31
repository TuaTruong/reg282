from concurrent.futures import thread
from tkinter import E
import uiautomator2 as u2
import time
import names
import random
import threading
import adb_control
import subprocess
lock = threading.Lock()

def reg(id):
    try:
        ip = random.choice(open("ip.txt").read().split("\n"))
        d = u2.connect(id)
        # d.shell(f"settings put global http_proxy {ip}")
        subprocess.call(f"adb.exe -s {id} shell settings put global http_proxy {ip}")
        # START
        d.app_clear("com.facebook.katana")
        time.sleep(2)
        d.app_start("com.facebook.katana", use_monkey = True)

        # CLICK CREATE ACCOUNT BUTTON 
        create_account_btn = d.xpath('//*[@content-desc="Create New Facebook Account"]')
        if create_account_btn.wait(60):
            create_account_btn.click()

        # CLICK NEXT BUTTON 
        next_btn = d.xpath('//*[@text="Next"]')
        if next_btn.wait(5):
            next_btn.click()

        # NAME
        time.sleep(1)
        firstname, lastname = names.get_full_name().split(" ")
        d.send_keys(firstname)

        d.xpath('//android.widget.ScrollView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]').click()
        d.send_keys(lastname)
        next_btn.click()


        # BIRTHDAY
        birthday_select = d.xpath('//android.widget.ScrollView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]')
        if birthday_select.wait(2):
            birthday_select.click()
        time.sleep(1)
        # swipe month 
        for i in range(random.randint(1,3)):
            d.swipe(0.3,0.6,0.3,0.3)
            time.sleep(1)
        # swipe day 
        for i in range(random.randint(1,3)):
            d.swipe(0.5,0.6,0.5,0.3)
            time.sleep(1)
        # swipe year 
        for i in range(random.randint(10,15)):
            d.swipe(0.7,0.3,0.7,0.6)
            time.sleep(1)
        d.xpath('//*[@resource-id="android:id/button1"]').click() # Click OK
        time.sleep(1)
        next_btn.click()

        # GENDER
        if d.xpath('//*[@text="Female"]').wait(2):
            d.xpath(f'//*[@text="{random.choice(["Female","Male"])}"]').click()
        next_btn.click()
        time.sleep(2)

        #EMAIL
        email = firstname+lastname+str(random.randint(1000000000,999999999999999)) + "@outlook.com"
        sign_up_email = d.xpath('//*[@text="Sign Up With Email Address"]')
        if sign_up_email.wait(2):
            sign_up_email.click()
        d.send_keys(email)
        next_btn.click()
        time.sleep(2)

        #PASSWORD
        password = "helloanhem" + str(random.randint(100,1000000000000))
        d.send_keys(password) 
        next_btn.click()
        time.sleep(2)

        # CHECK LIVE
        d.xpath('//*[@text="Sign Up"]').click()
        if d.xpath('//*[@content-desc="Continue"]').wait(30):
            threading.Thread(target=start,args={id,}).start()
            return email + "|"+ password
        else:
            threading.Thread(target=start,args={id,}).start()
            return ""
    except:
        print("Fail")
        threading.Thread(target=start,args={id,}).start()
            

def start(id):
    kq = reg(id)
    lock.acquire()
    if kq!="":
        open("success.txt","a").write(kq+"\n")
    else:
        print("uncatched")
    lock.release()




for device in adb_control.get_list_devices():
    threading.Thread(target=start,args={device,}).start()
    time.sleep(5)

