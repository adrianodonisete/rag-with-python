"""Shared embedding model configuration for the RAG pipelines."""

import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


def create_embedding_model() -> OpenAIEmbeddings:
    """Create OpenRouter-backed embeddings using its OpenAI-compatible API."""
    load_dotenv()

    return OpenAIEmbeddings(
        model="openai/text-embedding-3-small",
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url=os.getenv("OPENAI_URL", "https://openrouter.ai/api/v1"),
    )
