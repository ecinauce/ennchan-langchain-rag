# -*- coding: utf-8 -*-
from ennchan_search.core.model import BraveSearchEngine


def search(query, config=None):
    engine = BraveSearchEngine(config)
    results = engine.search(query)
    return results