import time
import requests

def RTT(URL):
    t1=time.time()

    r=requests.get(URL)

    t2=time.time()

    RTT=str(t2-t1)

    print "time in seconds are ", RTT


URL="http://www.facebook.com"
RTT(URL)
