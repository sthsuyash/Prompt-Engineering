import openai
import os
import time
from dotenv import load_dotenv, find_dotenv

# load environment variables
_ = load_dotenv(find_dotenv())

# set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


# function to get completion from OpenAI API
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = None
    while response is None:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
        except openai.error.RateLimitError:
            print("Rate limit exceeded. Waiting for 1 second...")
            time.sleep(1)

    return response.choices[0].message["content"]
