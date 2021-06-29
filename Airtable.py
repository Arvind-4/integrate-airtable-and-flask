import os
import requests
from dataclasses import dataclass

@dataclass()
class AirTable:
    base_id: str
    api_key: str
    table_name: str

    def create_records(self, email=None):
        if email is None:
            return False
        headers = {
            "Authorization": f"Bearer {self.api_key}",
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
        endpoint = f'https://api.airtable.com/v0/{self.base_id}/{self.table_name}'

        r = requests.post(endpoint, json=data, headers=headers)
        return r.status_code