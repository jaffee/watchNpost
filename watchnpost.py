from subprocess import call
from time import sleep
from twitter import tweet_pic
import os
import sys

dir_path = sys.argv[1]
known_files = os.listdir(dir_path)

while True:
    new_files = os.listdir(dir_path)
    for afile in new_files:
        if afile not in known_files:
            call(["killall", "Preview"])
            pic_file = os.path.join(dir_path, afile)
            call(["open", pic_file])
            tweet_pic(pic_file)
    known_files = os.listdir(dir_path)
    sleep(0.3)
