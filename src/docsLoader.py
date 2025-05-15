print("Accessing docs source...")
import bs4
from pathlib import Path
from langchain_community.document_loaders import WebBaseLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.configLoader import docs_source
from src.docsChecker import is_url, is_local_path
from src.webLoaderAdapter import WebLoaderAdapter
from src.textLoaderAdapter import TextLoaderAdapter


def load_documents(vector_store, source=docs_source):
    if is_url(source):
        loader = WebLoaderAdapter(source)

    elif is_local_path(source):
        loader = TextLoaderAdapter(source)

    else:
        raise ValueError("Invalid source type. Must be a URL or a local file path.")

    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_splits = text_splitter.split_documents(docs)

    # Index chunks
    _ = vector_store.add_documents(documents=all_splits)
    return all_splits
