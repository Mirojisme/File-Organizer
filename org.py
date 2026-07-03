import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


ORIGIN = r"C:\Users\Thaid\Downloads"  # Change this to your actual Downloads folder path
DESTINATION = r"C:\Users\Thaid\Downloads\Organized"  # Change this to your desired destination folder path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def organize_files():

    FILES = os.listdir(ORIGIN)

    for file in FILES:

        file_path = os.path.join(ORIGIN, file)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():

                if file_extension in extensions:
                    category_folder = os.path.join(DESTINATION, category)

                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)

                    shutil.move(file_path, os.path.join(category_folder, file))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(DESTINATION, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))

class FileHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            organize_files()

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