import requests
from typing import Dict, Any

class DHIS2Connector:
    """
    Simple DHIS2 Tracker connector.
    Open Source: does NOT store sensitive data, only interacts via API.
    """

    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url.rstrip("/")
        self.auth = (username, password)

    def get_tracker_events(self, program_id: str, org_unit: str) -> Dict[str, Any]:
        """
        Fetch Tracker events for a program and org unit
        """
        url = f"{self.base_url}/api/trackedEntityInstances.json"
        params = {
            "program": program_id,
            "orgUnit": org_unit,
            "paging": "false"
        }
        response = requests.get(url, params=params, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def send_tracker_event(self, program_id: str, org_unit: str, data: Dict[str, Any]):
        """
        Send a Tracker event
        """
        url = f"{self.base_url}/api/events"
        payload = {
            "program": program_id,
            "orgUnit": org_unit,
            "trackedEntityInstance": data.get("trackedEntityInstance"),
            "dataValues": data.get("dataValues", [])
        }
        response = requests.post(url, json=payload, auth=self.auth)
        response.raise_for_status()
        return response.json()
