import os 
import requests
import json


basic_token = os.environ.get('BASIC_TOKEN') or "d2lsbG1hbjAwMzpnYXZpcHBybzAwMw=="


def api_authentication():
    url = "http://localhost:5555/api/v1/tokens"
    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + basic_token
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    result = json.loads(response.text)
    token = result['token']
    return token

def api_get_users():
    url = "http://localhost:5555/api/v1/users"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result

def api_get_products():
    url = "http://localhost:5555/api/v1/products"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']
