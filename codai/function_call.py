# function_call.py
import os

from google.genai import types
from .functions.get_files_info import get_files_info
from .functions.get_file_contents import get_file_contents
from .functions.write_file import write_file 
from .functions.run_python_file import run_python_file




def call_function(function_call,working_directory,verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name} with arguments: {function_call.args}")
    else :
        print(f"Calling function: {function_call.name}")
    result = ""
    if function_call.name == "get_files_info":
        result = get_files_info(working_directory, **function_call.args)
    if function_call.name == "get_file_contents":
        result = get_file_contents(working_directory, **function_call.args)
    if function_call.name == "write_file":
        result = write_file(working_directory, **function_call.args)
    if function_call.name == "run_python_file":
        result = run_python_file(working_directory, **function_call.args)
    if function_call.name not in ["get_files_info","get_file_contents","write_file","run_python_file"]:    
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response={"error": f"Unknown function: {function_call.name}"} ,
            )
        ],
    )
    else :
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call.name,
            response={"result": result},
        )
    ],
)