import os
import shutil

from config import ORIGIN, DESTINATION, FILE_TYPES

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