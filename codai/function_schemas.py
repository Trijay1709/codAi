from google.genai import types
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_contents = types.FunctionDeclaration(
    name="get_file_contents",
    description="Reads and returns the contents of a specified file within the working directory.",

    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to read, relative to the working directory.",
            ),
        },
        
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file in the working directory and returns its output with python3 interpreter. Accepts additional cli arguments if needed as an array of strings.",

    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to execute, relative to the working directory. Must have a .py extension.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional array of strings of arguments to pass to the Python script.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
       
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates(and creates required parent directories if not present) or overwrites a file in the working directory with the provided content.",

    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to create or overwrite, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file.",
            ),
        },
    ),
)

available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_contents,
            schema_run_python_file,
            schema_write_file
        ]
    )