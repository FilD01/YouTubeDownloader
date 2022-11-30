import os
import time
import threading
import queue
import youtube_dl

ydl_opts = {
        'socket_timeout': 10,
        'ignore_errors': True,
        'add_metadata': True,
        'format': 'm4a',
        'outtmpl': './Downloads/%(playlist)s/%(title)s.%(ext)s',        
        'noplaylist' : True,

            }

maxthreads = 64 

urllist = []
while answer!='y' and answer!='n':
    print('Do you want to download a playlist?')
    answer = input('"y" or "n": ')
    if answer == 'y':
        print('Enter playlist URL: ')
        urllist.append(input())
        answer = None
        continue
    if answer == 'n':
        break
answer = None
# while not type(answer)==int:
#     print('How much threads?')
#     answer = int(input())
#     if not type(answer) ==  int:
#         maxthreads = 16
#     elif type(answer)==int:
#         maxthreads = anser 
urlIDlist = []
for url in urllist:
    Command = 'youtube-dl -i --get-id --flat-playlist --skip-download '+url
    urlIDlist += os.popen(Command).read().splitlines()
print(urlIDlist)
print(len(urlIDlist))
maxthreads = len(urlIDlist)
print('Start process')
tryno=0
def downloader(tryno):
    tryno = tryno + 1
    print('try no: '+str(tryno))
    exitFlag = 0

    class myThread(threading.Thread):
        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
        def run(self):
            print('starting'+ self.name)
            execute(self.name, self.q)
            print('exiting' + self.name)

    def download(data):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v='+data])
    def execute(threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print('%s processing %s' % (threadName, data))
                download(data)
            else:
                queueLock.release()
            time.sleep(1)
        return
    threadList = []
    for i in range(maxthreads):
        threadList.append('Thread_'+str(i))
    queueLock = threading.Lock()
    workQueue = queue.Queue(200)
    threads = []
    threadID = 1
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1
    queueLock.acquire()
    for urlID in urlIDlist:
        workQueue.put(urlID)
    queueLock.release()
    while not workQueue.empty():
        pass
    exitFlag = 1
    for t in threads:
        t.join()
    print('Exiting main thread')
    urlcount = len(urlIDlist)
    downloadcount = len([name for name in os.listdir('./Downloads/NA/') if os.path.isfile(os.path.join('./Downloads/NA/', name)) and name[0] != '.'])
    misseddownloads = urlcount-downloadcount 
    print('Urls: '+str(urlcount))
    print('Downloads: '+ str(downloadcount))
    print('missed downloads: '+str(misseddownloads))
    print('Completed? '+str(0>=misseddownloads))
    print('try no: '+str(tryno))
    if ((tryno <= 2 or misseddownloads > 0) and tryno <=4):
        downloader(tryno)
    else:
        print('Do you want to redownload?')
        answer = None
        while answer!='y' and answer!='n':
            print('Do you want to redownload?')
            answer = input('"y" or "n": ')
            if answer=='y':
                downloader(tryno) 
                break
            if answer == 'n':
                break
        answer = None
downloader(tryno)
print('FINISHED')
os.system('open ./Downloads/')
