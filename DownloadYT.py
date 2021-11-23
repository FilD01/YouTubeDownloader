import os

tbrURL = 'https://youtube.com/playlist?list=PLQ9De5XxSmaBwQOQs-79n7md7_YZJ-YFI'

def download(urllist):
    for url in urllist:
        Command = 'youtube-dl -f bestaudio[ext=m4a] -4 --socket-timeout 12 --ignore-errors --yes-playlist --add-metadata -o "./Downloads/%(playlist)s/%(title)s.%(ext)s" '+ url
        os.system(Command)
    return print('Download(s) finished')

urllist = []
answer = None
while answer!='y' and answer!='n':
    print('Do you wnat to download "to be rekordboxed"?')
    answer = input('"y" or "n": ')
    if answer=='y':
        urllist.append(tbrURL)
        break
    if answer == 'n':
        break
answer = None
while answer!='y' and answer!='n':
    print('Do you want to download other plalists?')
    answer = input('"y" or "n": ')
    if answer == 'y':
        print('Enter playlist URL: ')
        urllist.append(input())
        answer = None
        continue
    if answer == 'n':
        break
print('Starting download')
download(urllist)
os.system('open ./Downloads/')
print('Done')
