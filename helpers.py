import os
import getpass
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Prompt for key if missing
if not os.environ.get("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("OPENROUTER_API_KEY: ")

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]


llm = OpenRouter(
    api_key=os.environ["OPENROUTER_API_KEY"],
    model="anthropic/claude-3.5-sonnet",
    is_chat_model=True,
    is_function_calling_model=True,
)

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = llm
