import os
from dotenv import load_dotenv
from openai import AzureOpenAI

from llm_proxy import plotting_function_definitions, load_prompt_from_file

# Load environment variables
load_dotenv()


def get_azure_openai_response(messages, functions=None, enable_stream=False):
    """
    Sends a chat completion request to Azure OpenAI.
    """
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION_1"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_MODEL"),
        messages=messages,
        temperature=0.1,
        stream=enable_stream,
        functions=functions,
        function_call="auto"
    )

    return response


prompt_content = load_prompt_from_file()
messages = [{"role": "user", "content": prompt_content}]

stream_response = get_azure_openai_response(messages=messages,
                                            functions=[plotting_function_definitions],
                                            enable_stream=True)

for chunk in stream_response:
    print(chunk)
