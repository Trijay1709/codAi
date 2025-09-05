import os
import subprocess
def run_python_file(working_directory, file_path, args=[]):
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not absolute_file_path.startswith(absolute_working_dir):
        raise f'Error: "{file_path}" is not a valid file path in the working directory'
    if not os.path.isfile(absolute_file_path):
        raise f'Error: "{file_path}" does not exist or is not a file'
    if not file_path.endswith('.py'):
        raise f'Error: "{file_path}" is not a Python file'
    try:
        command = ['python3',file_path]
        if args:
            command.extend(args)
        
        output=subprocess.run(
            command ,cwd=absolute_working_dir,
            check=True,
            timeout=40,
            capture_output=True,
        )
        return_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """
        if output.stdout =="" and output.stderr == "":
            return f"File {file_path} executed successfully with no output."
        if output.returncode != 0:
            return f"Error running file {file_path}: {output.stderr.decode('utf-8')}"
        return return_string 
    except Exception as e:
        return f"Error running file {file_path}: {e}"   