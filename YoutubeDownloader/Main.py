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


url = sys.argv[1]
destination = sys.argv[2]

if 'http' not in url:
    url = 'http://' + url


playlist_URLs = crawl(url)

for link in playlist_URLs:
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(res="360p", file_extension='mp4').first()
        print("Downoading ..." + link)
        stream.download(destination)
        print("Finishing ..." + link)
        del yt
        del stream
    except:
        pass
