import os

def write_file(working_directory, file_path, content):
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not absolute_file_path.startswith(absolute_working_dir):
        raise f'Error: "{file_path}" is not a valid file path in the working directory'
    parent_dir = os.path.dirname(absolute_file_path)
    if not os.path.exists(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Error creating directory {parent_dir}: {e}"
    try:
        with open(absolute_file_path, 'w') as file:  
            file.write(content)
        return f"File {file_path} written successfully."
    except Exception as e:      
        return f"Error writing to file {file_path}: {e}"
    