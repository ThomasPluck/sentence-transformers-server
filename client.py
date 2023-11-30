import requests
import json

class NLPClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_embeddings(self, documents):
        """Sends documents to the server to get embeddings."""
        response = requests.post(
            f'{self.base_url}/embedding',
            json={"documents": documents}
        )
        return response.json()

    def perform_semantic_search(self, query, documents):
        """Sends a query and documents to the server for semantic search."""
        response = requests.post(
            f'{self.base_url}/semantic_search',
            json={"query": query, "documents": documents}
        )
        return response.json()
