import os

tbrURL = 'https://youtube.com/playlist?list=PLQ9De5XxSmaBwQOQs-79n7md7_YZJ-YFI'

def download(urllist):
    for url in urllist:
        Command = 'youtube-dl -f bestaudio[ext=m4a] -4 --socket-timeout 12 --ignore-errors --yes-playlist --add-metadata -o "./Downloads/%(playlist)s/%(title)s.%(ext)s" '+ url
        os.system(Command)
    return print('Download(s) finished')
urllist = []
urllist.append(tbrURL)
print('Starting download')
download(urllist)
os.system('open ./Downloads/')
print('Done')
