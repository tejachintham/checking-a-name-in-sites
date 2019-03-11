import requests
from threading import Thread
from queue import Queue
concurrent = 200
def doWork():
    while True:
        url = q.get()
        urlstatus = getStatus(url)
        q.task_done()

def getStatus(myurl):
    try:
        murl="http://"+myurl
        htmlsource = requests.get(murl,timeout=60)
        htmlsource = str(htmlsource.text)
        if "xxxxxxxxe" in htmlsource:
            g=open("has.txt","a")
            g.write((myurl.split("/wp-login.php"))[0])
            g.write("\n")
            g.close
        else:
            g=open("dont.txt","a")
            g.write((myurl.split("/wp-login.php"))[0])
            g.write("\n")
            g.close
    except:
        g=open("errors.txt","a")
        g.write((myurl.split("/wp-login.php"))[0])
        g.write("\n")
        g.close 

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    with open("31-dec.txt") as infile:
        for line in infile:
            line=line.strip()
            lin=line+"/wp-login.php"
            q.put(lin)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
