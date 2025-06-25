import requests

class APIClient:
    """Simulate and extermnal API Client"""
    def get_user_data(self,user_id):
        response=requests.get(f"https://gorest.co.in/public/v2/users/{user_id}")
        if response.status_code==200:
            return response.json()
        raise ValueError("API requests failed")

class UserService:
    """Uses APIClient to fetach user data and process it."""
    def __init__(self,api_client):
        self.api_clent=api_client

    def get_username(self,user_id):
        """Featched a user and returns therie username in uppercase"""
        user_data=self.api_clent.get_user_data(user_id) # Calls API CLient
        return user_data["name"].upper()