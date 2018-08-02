import requests
import threading



print "STRAWPOLL.COM BASIC VOTE REQUESTS"
print "CREATED BY QIUBY ZHUKHI"
print "--- [ PBM TEAM ] --- "
pid = "sg7rydb7"
vote = "check20275143"

def strawpoll(pid, vote):
    with requests.session() as c:
        data = {"pid":pid, "oids":vote}
        url = "https://strawpoll.com/"+pid
        print "Cek Nama: "+vote
        req = c.get(url)
        h = {"Origin": "https://strawpoll.com",
             "X-Requested-With": "XMLHttpRequest",
             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.185.1002 Safari/537.36",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "Referer": "https://strawpoll.com/"+pid,
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "en-US,en;q=0.8"}
        resp = c.post("https://strawpoll.com/vote?", data=data, headers=h)
        c.get("https://strawpoll.com/refresh")
        c.cookies.clear()
        c.cookies.keys()
def start():
    list = []
    for i in range(0,100):
        thread = threading.Thread(target=strawpoll, args=(pid,vote), name="start {}".format(i))
        list.append(thread)
        thread.start()
    for _ in list:
        _.join()
if __name__ == "__main__":
    jml = int(raw_input("Jumlah Vote: "))
    for _ in range(0,jml):
        start()
