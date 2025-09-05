#main.py

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from function_call import call_function
from config import gemini_config

max_iterations = 20
def main():    
    load_dotenv()
    verbose = False
    api_key = os.environ.get("GEMINI_API_KEY")
    if len(sys.argv) < 2:
        print("I need a PROMPT argument")
        sys.exit(1)
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True

    prompt = sys.argv[1]
    
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
                function_call_response = call_function(function_call,verbose)
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