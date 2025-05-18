from brave import Brave
from typing import Optional, List, Dict, Any

from ennchan_search.core.interfaces import SearchEngine
from ennchan_search.extractor.extractorModel import WebResultExtractor

class BraveSearchEngine(SearchEngine):
    def __init__(self, config: Optional[Dict[str, Any]]):
        self.config = config
        if not self.config:
            self.brave = Brave()
        else:
            self.brave = Brave(api_key=self.config["BRAVE_API_KEY"])


    def extract_content(self, url: str) -> Optional[str]:    
        """Extract main content from a URL - simplified version"""
        output = WebResultExtractor(url)
        output.request_content()
        return output.result


    def process_results(self, results: Dict[str, Any]) -> List[Dict[str, Any]]:
        # Get only important fields
        pre_proc = results["web"]["results"]
        pre_proc = [{
            "title": result["title"],
            "url": result["url"],
            "description": result["description"],
        } for result in pre_proc]

        # Extract content from each URL
        output = []
        # Can be threaded for performance
        for result in pre_proc:
            print(f"Processing {result['url']}")
            url = result["url"]
            content = self.extract_content(url)
            
            # Collate contents if exist
            if content:
                output.append({
                    "title": result["title"],
                    "url": url,
                    "description": result["description"],
                    "content": content
                })
        
        return output


    def search(self, query: str) -> List[Dict[str, Any]]:
        search_results = self.brave.search(q=query, raw=True)

        output = self.process_results(search_results)
        return output