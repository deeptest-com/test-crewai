import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from openai import AzureOpenAI

model = "gpt-4"

def get_conf_azure():
    _ = load_dotenv(find_dotenv())

    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version=os.getenv("AZURE_OPENAI_VERSION"),
    )

    return client
