import urllib.request as fr
import os


msg = ""
num = ""
password = ""

def send_sms():



    #print (t1 + t2)
    f = fr.urlopen(accURL)
    s = f.read()
    print(s)
    print(type(s))

send_sms()
