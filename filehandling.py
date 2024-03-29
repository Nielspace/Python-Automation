from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import os 

class myFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename == ".jpg":
                pass
            src = folder_to_track + '/' + filename
            new_destination = folder_destination + '/' + filename
            os.rename(src, new_destination)
            

folder_to_track = '/Users/nielspace/Desktop/empty'
folder_destination = '/Users/nielspace/Desktop/test'

event_handler = myFileHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()