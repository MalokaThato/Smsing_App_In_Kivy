import urllib.request as fr
import os


msg = ""
num = ""
password = ""

def send_sms():

    #t1 = "http://www.winsms.co.za/api/batchmessage.asp?User=malokathato@gmail.com&Password=G4T1989tg$&Deliver=No&Message=" + msg
    #t2 = "&Numbers=0739548248"
    print(password)
    accURL = "http://www.winsms.co.za/api/batchmessage.asp?User=malokathato@gmail.com&Password=%s&Deliver=No&Message=%s&numbers=%s" %(password,msg,num)
    #print (t1 + t2)
    f = fr.urlopen(accURL)
    s = f.read()
