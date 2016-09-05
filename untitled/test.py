from urlparse import urlparse
from threading import Thread
import httplib, sys, json
from Queue import Queue

concurrent = 200

def doWork():
    while True:
        url = q.get()
        response = getStatus(url)
        print json.loads(response)['itemCount']
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        # print url
        conn = httplib.HTTPConnection(url.netloc)
        # print url.netloc
        conn.request("GET", url.path+'?'+url.query)
        # print url.netloc + url.path+'?'+url.query
        res = conn.getresponse()
        # print res.read();
        return res.read()
    except:
        return "error", ourl



q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:
    for url in open('urllist.txt'):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)