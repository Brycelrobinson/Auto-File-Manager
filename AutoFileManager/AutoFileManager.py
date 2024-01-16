#!/usr/bin/env python3
import os
import shutil
from datetime import datetime
from datetime import date
from time import sleep

documents = ["docx", "doc", "ppt", "odt", "odf", "rtf", "pdf", "txt", "ppt", "pptx", "odp", "svg"]
pictures = ["jpg", "png", "gif", "jpeg"]
videos = ["mp4", "mov", "wmv"]
music = ["mp3", "m4a", "wav", "wma"]
code = ["java", "cpp", "c", "py", "cs", "php", "vb", "html", "css", "scss", "js"]



while True:
    files = os.listdir("/home/bryce/Downloads")

    for file in files :
        dest_dir = ""
        
        if ".~lock." not in file:
            ext = (file.split(".")[-1]).lower()
            file_path = os.path.join("/home/bryce/Downloads", file)
            
            
            if ext in documents:
                if not os.path.exists("/home/bryce/Documents/" + file):
                    shutil.move(file_path, "/home/bryce/Documents/")
                    dest_dir = "/home/bryce/Documents/"
                else:
                    continue
            elif ext in pictures:
                if not os.path.exists("/home/bryce/Pictures/" + file):
                    shutil.move(file_path, "/home/bryce/Pictures/")
                    dest_dir = "/home/bryce/Pictures/"
                else:
                    continue
            elif ext in videos:
                if not os.path.exists("/home/bryce/Videos/" + file):
                    shutil.move(file_path, "/home/bryce/Videos/")
                    dest_dir = "/home/bryce/Videos/"
                else:
                    continue
            elif ext in music:
                if not os.path.exists("/home/bryce/Music/" + file):
                    shutil.move(file_path, "/home/bryce/Music/")
                    dest_dir = "/home/bryce/Music/"
                else:
                    continue
            elif ext in code:
                if not os.path.exists("/home/bryce/Code/" + file):
                    shutil.move(file_path, "/home/bryce/Code/")
                    dest_dir = "/home/bryce/Code/"
                else:
                    continue
            else:
                continue
                
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            today = date.today()
            current_date = today.strftime("%b-%d-%Y")
            
            output = "Filename: "+ file +  "\nDestination: " + dest_dir + "\nDate: " + current_date + "\nTime Stamp: " + current_time + "\n\n"
 
            
            file1 = open('/home/bryce/PersonalProjects/AutoFileManager/DownloadLog.txt', 'a')
            file1.writelines(output)
            file1.close()  
    del files
    sleep(15)
