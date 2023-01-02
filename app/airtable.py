import os
import requests
from dataclasses import dataclass

from .constants import (
    BASE_URL,
    VERSION,
)

@dataclass()
class AirTable:
    baseId: str
    apiKey: str
    tableName: str
    def create_records(self, email=None):
        if email is None:
            return 404
        headers = {
            "Authorization": f"Bearer {self.apiKey}",
            "Content-Type": "application/json"
        }
        data = {
            'records':[
                {
                    'fields':{
                        'email': email,
                    }
                }
            ]
        }
        endpoint = f'{BASE_URL}/{VERSION}/{self.baseId}/{self.tableName}'
        r = requests.post(endpoint, json=data, headers=headers)
        return r.status_code