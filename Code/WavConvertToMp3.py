import os
import subprocess

# 走訪現在所在的目錄
#os.walk()=>回傳 現在所在資料夾的位置、現在資料夾下所有目錄的名字、現宰資料夾下所有檔案的名字(root,dir,filename)
for dirPath, dirNames, fileName in os.walk("./"):
    for file_name in fileName:
        if file_name.endswith('.wav') or file_name.endswith('.WAV'):
            print ("it's converting file : "+file_name)
            subprocess.call('ffmpeg -i {} -vn -ar 44100 -ac 2 -ab 192k -f mp3 {}.mp3'.format(file_name,file_name[:-4]),shell=True)