import re
import sys
import time
import urllib.error
import urllib.request
from collections import OrderedDict
from pytube import YouTube

playlist_URLs = []

def crawl(url):
    sTUBE = ''
    cPL = ''
    amp = 0
    final_url = []
    all_url = []

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]

    else:
        print('Incorrect Playlist.')
        exit(1)

    try:
        yTUBE = urllib.request.urlopen(url).read()
        sTUBE = str(yTUBE)
    except urllib.error.URLError as e:
        print(e.reason)

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, sTUBE)

    if mat:

        for PL in mat:
            yPL = str(PL)
            if '&' in yPL:
                yPL_amp = yPL.index('&')
            final_url.append('http://www.youtube.com/' + yPL[:yPL_amp])

        all_url = list(OrderedDict.fromkeys(final_url))

        # i = 0
        # while i < len(all_url):
        #     sys.stdout.write(all_url[i] + '\n')
        #     time.sleep(0.04)
        #     i = i + 1
    return all_url

# if len(sys.argv) < 2 or len(sys.argv) > 2:
#     print('USAGE: python3 youParse.py YOUTUBEurl')
#     exit(1)
#
# else:
#     url = sys.argv[1]
#     if 'http' not in url:
#         url = 'http://' + url
#     #crawl(url)
#     crawl("https://www.youtube.com/playlist?list=PLo9MNzK_jQY-QVtFYW9wx4HSewIlbtikJ")

playlist_URLs = crawl("https://www.youtube.com/playlist?list=PLo9MNzK_jQY-QVtFYW9wx4HSewIlbtikJ")

for link in playlist_URLs:
    print(link)
    #yt = YouTube(link)

    try:
        yt = YouTube(link)
        stream = yt.streams.first()
        print("Downoading ..." + link)
        stream.download("C:/Users/itsix/Desktop/youtube_downloads")
        print("Finishing ..." + link)
        del yt
        del stream
    except:
        pass
