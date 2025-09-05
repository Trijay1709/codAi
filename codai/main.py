#main.py

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from .function_call import call_function
from .config import gemini_config
import argparse

max_iterations = 20
from dotenv import load_dotenv
import os

def resolve_api_key(args):
    load_dotenv()  # loads from .env if present
    if args.key:  # CLI override
        return args.key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini API key not found. Use -k or set GEMINI_API_KEY.")
    return api_key
import os

def resolve_working_dir(args):
    working_dir = args.dir if args.dir else os.getcwd()
    if not os.path.isdir(working_dir):
        raise ValueError(f"Invalid directory: {working_dir}")
    return working_dir


def main():    
    # CLI arguments
    parser = argparse.ArgumentParser(
        description="codai - A CLI coding assistant powered by Gemini"
    )
    parser.add_argument("prompt", help="Your prompt for codai")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("-k", "--key", help="Pass Gemini API key directly (overrides .env/env var)")
    parser.add_argument("-d", "--dir", default=os.getcwd(), help="Working directory (default: current directory)")
    args = parser.parse_args()

    # Resolve config
    api_key = resolve_api_key(args)
    working_dir = resolve_working_dir(args)

    # Load .env if present
    load_dotenv()

    # Get API key (priority: CLI arg > env var > .env)
    api_key = args.key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY is missing. Provide with --key or set it in .env/env.")
        sys.exit(1)

    prompt = args.prompt
    verbose = args.verbose
    
    messages = [ 
        types.Content(role = "user",parts=[types.Part(text=prompt)])
    ]
    
    for i in range(max_iterations):
        
        gemini_client = genai.Client(api_key=api_key)
        response = gemini_client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=gemini_config,
        )
        if response.candidates :
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)
        if response.function_calls:
            for function_call in response.function_calls:
                function_call_response = call_function(function_call,working_dir,verbose)
                messages.append(function_call_response)
                # print(function_call_response.parts[0].response["result"])
            
        else:
            print(response.text)
            return
        
        if response is None or response.usage_metadata is None:
            print("No response received from the model.")
            return
        if verbose : 
            print(f"User_prompt: {prompt}")
            print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
        
main()