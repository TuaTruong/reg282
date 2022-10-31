from time import sleep
import uiautomator2 as u2
import adb_control
import threading
def clear(i):
    d = u2.connect(i)
    d.app_stop_all()
    sleep(2)
for i in adb_control.get_list_devices():
    threading.Thread(target=clear, args={i,}).start()
    sleep