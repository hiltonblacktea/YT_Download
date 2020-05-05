#python 下載youtube影音檔(mp4 OR mp3) 20190607 completed
#使用youtube_dl將音檔載下(mp4),再將mp4轉成mp3

import subprocess
import wx
import os
import pygame
from pydub import AudioSegment


#刪除MP4檔
def deleteMP4(path):
    fileList = os.listdir(path)
    for filename in fileList:
        if filename.endswith(".mp4"):
            print("正在刪除文件:\n",filename,'\n')
            os.remove('D:/python/YT_Download/Music/%s ' % filename)
            print('已經成功刪除',filename,'\n')
# 下載整份影片清單       
def makeMP4list(path,musicurl):
    try:
        all = 'youtube-dl  -f mp4 ' + musicurl
        p = subprocess.Popen(all)
        p.wait()
        """
        p = subprocess.Popen(
        'youtube-dl  -f mp4 %s ' % musicurl,
        #['youtube-dl',musicurl],
        bufsize=0,
        stdin=None, stdout=None, stderr=None,
        shell=True, 
        cwd=path, env=None,
        universal_newlines=False)
        p.wait()
        """
        print('down')
    except Exception as e:
        print('出錯原因是 %s' % str(e))
#產生MP4檔(單個)
def makeMP4(path,musicurl,mp3ormp4):
    try:
        url = 'youtube-dl  -f mp4 ' + musicurl
        """
        p = subprocess.Popen(
        url ,
        #['youtube-dl',musicurl],
        bufsize=0,
        stdin=None, stdout=None, stderr=None,
        shell=True, 
        cwd=path, env=None,
        universal_newlines=False)
        p.wait()
        """
        p = subprocess.Popen(url,cwd=path)
        p.wait()
        if mp3ormp4 == 'mp4':
            print('mp4已經下載')
            print('-----------------------------------------------------------')
            main()
    except Exception as e:
        print('出錯原因是 %s' % str(e))
#產生MP3檔
def makeMP3(path,musicurl,mp3ormp4):
    makeMP4(path,musicurl,mp3ormp4)
    #從資料夾取得mp4
    fileList = os.listdir(path)
    for filename in fileList:
        if filename.endswith(".mp4"):   
            print('找到檔案:\n',filename)
            MP4music = filename
            MP3music = MP4music.replace('.mp4','',1)
            #匯出mp3檔
            music = AudioSegment.from_file("D:/python/YT_Download/Music/%s " % MP4music,"mp4")
            music.export("D:/python/YT_Download/Music/%s.mp3 " % MP3music , format="mp3")
    
    MP4DeleteOrNot = input('\nmp4檔是否保留?(y or n)\n')
    if MP4DeleteOrNot == 'n':
        deleteMP4(path)
        print('-----------------------------------------------------------')
        main()
    else:
        print('-----------------------------------------------------------')
        main()
def main():
    #檔案儲存點
    path = 'D:/python/YT_Download/Music'
    #youtube網址
    musicurl = input('請輸入網址:\n')
    #makeMP4list(path,musicurl)
    mp3ormp4 = input('請輸入格式(mp3或是mp4):\n')
    if mp3ormp4 == 'mp4':
        makeMP4(path,musicurl,mp3ormp4)
    elif mp3ormp4 == 'mp3':
        makeMP3(path,musicurl,mp3ormp4)
    else:
        print('格式選擇錯誤')
    
    main()
main()

#subprocess.popen()參數: https://www.cnblogs.com/zhoug2020/p/5079407.html
#AudioSegment文件:https://github.com/jiaaro/pydub/blob/master/API.markdown
#youtube-dl文件:https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
# 2020/01/16 更新 : pip install --upgrade youtube-dl(出現 this video is unavailable 錯誤)
# 2020/02/07 可下載整份影片清單