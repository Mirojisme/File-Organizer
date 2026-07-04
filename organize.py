import os
import shutil

from config import IGNORED_EXTENSIONS, ORIGIN, DESTINATION, FILE_TYPES

def organize_files():

    FILES = os.listdir(ORIGIN)

    for file in FILES:

        file_path = os.path.join(ORIGIN, file)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in IGNORED_EXTENSIONS:
                continue
            moved = False

            for category, extensions in FILE_TYPES.items():

                if file_extension in extensions:
                    category_folder = os.path.join(DESTINATION, category)
                    file_destination_path = os.path.join(category_folder, file)

                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    
                    if os.path.exists(file_destination_path):
                        print(f"'{file}' already exists")
                        file_destination_path = unique_file_name(category_folder, file)

                        
                    shutil.move(file_path, file_destination_path)
                    
                    moved = True
                    print(f"Moved '{file}' to '{category_folder}'")
                    break
                    
            
            
            if not moved:
                other_folder = os.path.join(DESTINATION, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved '{file}' to '{other_folder}'")
            

def unique_file_name(destination_path, filename):
    name, extension = os.path.splitext(filename)
    destination = os.path.join(destination_path, filename)
    
    counter = 1
    while os.path.exists(destination):
        new_file_name = f"{name}_{counter}{extension}"
        destination = os.path.join(destination_path, new_file_name)
        counter += 1
    
    return destination