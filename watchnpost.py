from subprocess import call
from time import sleep
import os
import sys

dir_path = sys.argv[1] 
Known_files = os.listdir(dir_path)

while True:
    new_files = os.listdir(dir_path)
    for file in new_files:
        if file not in known_files:
            call(["killall", "Preview"])
            call(["open", dir_path + file])
    known_files = os.listdir(dir_path)
    sleep(0.3)
