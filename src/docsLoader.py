print("Accessing docs source...")
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.configLoader import docs_source

def load_documents(vector_store):
    # Load and chunk contents of the blog
    loader = WebBaseLoader(
        web_paths=(docs_source,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("mw-content-container")
            )
        ),
    )
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_splits = text_splitter.split_documents(docs)

    # Index chunks
    _ = vector_store.add_documents(documents=all_splits)
    return all_splits
