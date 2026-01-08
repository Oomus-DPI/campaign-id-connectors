import requests
from typing import Dict, Any

class OpenSRPConnector:
    """
    Simple OpenSRP API connector.
    Open Source: Only interacts with open endpoints.
    """

    def __init__(self, base_url: str, token: str = None):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def get_headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get_client(self, client_id: str) -> Dict[str, Any]:
        """
        Retrieve client data by ID (non-sensitive)
        """
        url = f"{self.base_url}/rest/client/{client_id}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def send_visit_data(self, visit_data: Dict[str, Any]):
        """
        Send visit data
        """
        url = f"{self.base_url}/rest/visit"
        response = requests.post(url, json=visit_data, headers=self.get_headers())
        response.raise_for_status()
        return response.json()
