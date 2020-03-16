import urllib2
import requests

targetIP = "http://192.168.1.4"

class PassAttempt:
    def __init__(self, u = "", p = "",): 
        self.uName = u
        self.password = p
    
    def tryPass(self, target, pmanage):
        pmanage.add_password(None, targetIP, self.uName, self.password)
        handler = urllib2.HTTPDigestAuthHandler(pmanage)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        try:
            a = urllib2.urlopen(targetIP)
            return True
        except:
            return False
        

