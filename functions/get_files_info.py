import os
from google.genai import types
def get_files_info(working_directory, directory="."): 
    absolute_working_dir = os.path.abspath(working_directory)
    
    absolute_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not absolute_directory.startswith(absolute_working_dir):
        raise f'Error: "{directory}" is not a directory'
    contents = os.listdir(absolute_directory)
    final_response = ""
    for content in contents:
        content_path = os.path.join(absolute_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path) 
        final_response+=f'{content}: is direcotry = {is_dir},Size:{size} bytes\n'
    return final_response


