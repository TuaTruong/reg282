list_ip = open("ip.txt","r").read().split("\n")
open("ip.txt","w").write("")
for i in list_ip:
    open("ip.txt","a").write(i.split("|")[0]+"\n")