import os
import getpass
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Prompt for key if missing
if not os.environ.get("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("OPENROUTER_API_KEY: ")

if not os.environ.get("MODEL_NAME"):
    os.environ["MODEL_NAME"] = getpass.getpass("MODEL_NAME: ")

if not os.environ.get("EMBED_MODEL_NAME"):
    os.environ["EMBED_MODEL_NAME"] = getpass.getpass("EMBED_MODEL_NAME: ")

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
MODEL_NAME = os.environ["MODEL_NAME"]
EMBED_MODEL_NAME = os.environ["EMBED_MODEL_NAME"]


llm = OpenRouter(
    api_key=OPENROUTER_API_KEY,
    model=MODEL_NAME,
    is_chat_model=True,
    is_function_calling_model=True,
)

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)
Settings.llm = llm
