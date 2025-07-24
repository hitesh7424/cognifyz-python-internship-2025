"""
Task 03: Automate a Task
Identify a repetitive task, such as data
processing, file management, or report
generation, and develop a script to
automate it using Python. This task will
showcase their problem-solving skills and
familiarity with Python's automation
capabilities.
"""

# File Management Tool in Python

import os
import shutil
from datetime import datetime

# Change this to the path you want to organize
# lets organize my downloads folder
# "C:\Users\hites\Downloads"
TARGET_FOLDER = r"C:\Users\hites\Downloads"


# get all the files recursively
def get_all_files_in_folder(folder_path):
    all_files = []

    for f in os.listdir(folder_path):
        full_path = os.path.join(folder_path, f)
        if os.path.isfile(full_path):
            all_files.append(full_path)
        elif os.path.isdir(full_path):
            all_files.extend(get_all_files_in_folder(full_path))

    return all_files


# get all the files
def get_files_in_folder(folder_path):
    '''
    gets all the files at the folder path
    '''
    file_paths = []
    files = os.listdir(folder_path)
    for f in files:
        full_path = os.path.join(folder_path, f)
        if os.path.isfile(os.path.join(folder_path, f)):
            file_paths.append(full_path)

    return file_paths


# get the file into (modified_date, category)
def get_file_info(filename):
    '''
    extracts the basic file info that is modified date and extention of the file
    '''
    timestamp = os.path.getmtime(filename)
    modified_date = datetime.fromtimestamp(timestamp).strftime("%Y-%m")
    extension = os.path.splitext(filename)[1][1:].lower() or "no_extension"

    return extension, modified_date


# Define file type to folder mapping
FILE_TYPE_FOLDERS = {
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "svg"],
    "Documents": ["pdf", "docx", "doc", "txt", "pptx", "xlsx", "xls", "ppt"],
    "Videos": ["mp4", "mov", "avi", "mkv", "flv"],
    "Music": ["mp3", "wav", "aac", "ogg"],
    "Archives": ["zip", "rar", "7z", "tar", "gz"],
    "Programs": ["exe", "msi"],
    "Scripts": ["py", "js", "sh", "bat"],
}


# extracts the file category based on the extension
def get_file_category(extension):
    '''
    gives category to the file based on the extention of extention is not in the list then it will be categories to Others
    '''
    for category, extensions in FILE_TYPE_FOLDERS.items():
        if extension in extensions:
            return category

    return "Others"


# function to make directory
def make_directory(path):
    '''
    simple function to create directory if the directory already exists then it will no give any erros '''
    try:
        os.makedirs(path, exist_ok=True)
        return f"Folder Created: {path}"
    except Exception as e:
        return f"Some error occured: {e}"


def get_safe_filename(dest_dir, filename):
    '''
    this to get a safe file name to avoid overwriting the existing file
    '''
    name, ext = os.path.splitext(filename)
    counter = 1

    new_filename = filename
    dest_path = os.path.join(dest_dir, new_filename)

    while os.path.exists(dest_path):
        new_filename = f"{name}_{counter}{ext}"
        dest_path = os.path.join(dest_dir, new_filename)
        counter += 1

    return new_filename


# to move file
def move_file(source_path, destination_path):
    '''
    move the file to the destination folder'''
    try:
        shutil.move(source_path, destination_path)
    except Exception as e:
        print(f"Error moving {source_path}: {e}")


# main function to impleemtn the all process
def main():
    '''
    this main excutes all the function in order to perform the file management
    also logs the processes to review the process or any error occured
    '''
    history_log = []

    for full_path in get_files_in_folder(TARGET_FOLDER):
        filename = os.path.basename(full_path)
        extension, modified_date = get_file_info(full_path)

        category = get_file_category(extension)

        dest_path = os.path.join(TARGET_FOLDER, category, modified_date)
        safe_filename = get_safe_filename(dest_path, filename)
        dest_file = os.path.join(dest_path, safe_filename)

        source_file = os.path.join(full_path)

        dir_log = make_directory(dest_path)
        log1 = f"[{datetime.now()}] {dir_log}"
        print(log1)
        history_log.append(log1)
        move_file(source_file, dest_file)
        log2 = f"[{datetime.now()}] Moved: {source_file} → {dest_file}"
        print(log2)
        history_log.append(log2)

    make_directory(".logs")
    with open(".logs/history.log", "a", encoding="utf-8") as log_file:
        for log in history_log:
            log_file.write(str(log) + "\n")


if __name__ == "__main__":
    '''
    here the main function is executed
    
    lets organize my downloads folder which is cluttered
    '''
    
    main()
    
'''
SO the files are managed 😊
'''
