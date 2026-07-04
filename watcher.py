from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from organize import organize_files, ORIGIN


class FileHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            organize_files()

def start_monitoring():
    observer = Observer()
    observer.schedule(FileHandler(), ORIGIN, recursive=False)
    try:
        observer.start()
        print("Monitoring started. Press Ctrl+C to stop.")
        while True:
            print("Monitoring...")
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()