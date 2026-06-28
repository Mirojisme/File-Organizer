import os
import shutil


ORIGIN = r"C:\Users\Thaid\Downloads"  # Change this to your actual Downloads folder path
DESTINATION = r"C:\Users\Thaid\Downloads\Organized"  # Change this to your desired destination folder path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

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

