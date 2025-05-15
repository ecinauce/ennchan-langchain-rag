import bs4
from src.interfaces import DocLoader
from langchain_community.document_loaders import WebBaseLoader


class WebLoaderAdapter(DocLoader):
    def __init__(self, url):
        self.url = url


    def load(self):
        return WebBaseLoader(
            web_paths=(self.url,),
            bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("mw-content-container")
                )
            ),
        )