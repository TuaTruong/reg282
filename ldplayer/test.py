import uiautomator2 as u2
import adb_control

print(adb_control.get_list_devices())
d = u2.connect()
print(d.info)
