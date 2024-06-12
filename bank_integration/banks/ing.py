import requests
import json

class ING:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self.get_access_token()

    def get_access_token(self):
        auth_url = "https://api.ing.com/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials", "client_id": self.client_id, "client_secret": self.client_secret}
        response = requests.post(auth_url, headers=headers, data=data)
        return response.json()["access_token"]

    def get_accounts(self):
        api_url = "https://api.ing.com/accounts"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(api_url, headers=headers)
        return response.json()

    def get_account(self, account_id):
        api_url = f"https://api.ing.com/accounts/{account_id}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(api_url, headers=headers)
        return response.json()

    def initiate_transaction(self, account_id, amount, recipient):
        api_url = "https://api.ing.com/transactions"
        headers = {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}
        data = {"account_id": account_id, "amount": amount, "recipient": recipient}
        response = requests.post(api_url, headers=headers, json=data)
        return response.json()

    def get_transactions(self):
        api_url = "https://api.ing.com/transactions"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(api_url, headers=headers)
        return response.json()
