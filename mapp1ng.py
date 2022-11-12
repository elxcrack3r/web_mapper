import queue
import threading
import os
import urllib

threads = 10

target = "https://www.newforum.eu"
directory = "/usr/share/wordlists/common.txt"
filters = [".jpg", ".gif", ".png", ".css"]

os.chdir(directory)

