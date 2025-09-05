import os
from config import MAX_CHARS

def get_file_contents(working_directory, file_path):

    absolute_working_dir = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not absolute_file_path.startswith(absolute_working_dir):
        raise f'Error: "{file_path}" is not a valid file path in the working directory'
    if not os.path.isfile(absolute_file_path):
        raise f'Error: "{file_path}" does not exist or is not a file'
    file_content_string = ""
    with open(absolute_file_path, 'r') as file:
        file_content_string = file.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += "\n... (truncated to first 10,000 characters)"
    return file_content_string