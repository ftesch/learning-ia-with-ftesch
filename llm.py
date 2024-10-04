import os
from dotenv import load_dotenv
load_dotenv(override=True)  # take environment variables from .env.

from langchain_openai import AzureChatOpenAI

api_version = os.getenv("AZURE_OPENAI_API_VERSION")

print(api_version)

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o",
    api_version= api_version,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

response = llm.invoke("Conte-me uma piada")
for chunk in response:
    print(chunk, end="", flush=True)