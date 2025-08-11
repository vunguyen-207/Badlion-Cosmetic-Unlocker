import os
import shutil
import requests
import colorama
import pystyle
import time
from time import sleep
import sys

definedll = "https://github.com/iaanbennett/badlion-unlocker/releases/download/0.0.1/version.dll"

definethatjson = "https://github.com/iaanbennett/badlion-unlocker/releases/download/0.0.1/cosmetics.json"

definedefaulttargetfolder = os.path.join(os.path.expanduser("~"), r"AppData\Roaming\Badlion Client\Data")

definejsondeservertobelocation = r"C:\cosmetics.json"

getdlldownloadpath = os.path.join(os.getenv("TEMP"), "version.dll")


def dodownloadthings(url, savepath):
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    print(f"\033[1;39m[\033[0;31mvu\033[1;39m] Đang unlock.")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(savepath, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"\033[1;39m[\033[0;31mvu\033[1;39m] Đã lưu requirements.")
    
try:
    dodownloadthings(definedll, getdlldownloadpath)
    
    getalljdkjrefolder = [
        os.path.join(definedefaulttargetfolder, folder)
        for folder in os.listdir(definedefaulttargetfolder)
        if os.path.isdir(os.path.join(definedefaulttargetfolder, folder)) and (folder.startswith("jre") or folder.startswith("jdk"))
    ]
    
    for folder in getalljdkjrefolder:
        getbinfolderinsidethepaths = os.path.join(folder, "bin")
        
        if os.path.isdir(getbinfolderinsidethepaths):
            applyon = os.path.join(getbinfolderinsidethepaths, "version.dll")
            shutil.copy2(getdlldownloadpath, applyon)
            print(f"\033[1;39m[\033[0;31mvu\033[1;39m] Unlocking")
            
        else:
            print(f"\033[1;39m[\033[0;31mvu\033[1;39m] Skip {folder} do k thấy folder yêu cầu..")
            
    dodownloadthings(definethatjson, definejsondeservertobelocation)
    
    print("\033[1;39m[\033[0;31mvu\033[1;39m] Đã mở toàn bộ cosmetics. Bạn có thể vào game.")
    time.sleep(5)
    sys.exit(1)
except Exception as e:
    print(f"\033[1;39m[\033[0;31mvu\033[1;39m] Run me as administrator fucktard.")
