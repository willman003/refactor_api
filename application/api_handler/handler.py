import os 
import requests
import json

basic_auth = os.environ.get('BASIC_TOKEN') or "d2lsbG1hbjAwMzpnYXZpcHBybzAwMw=="


def api_authentication():
    url = "http://localhost:5555/api/v1/tokens"
    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + basic_auth
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    result = json.loads(response.text)
    token = result['token']
    return token

#API_USER
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

#API_CUSTOMER
def api_get_customer(id):
    url = "http://localhost:5555/api/v1/customers/"+str(id)

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']


def api_get_list_customer():
    url = "http://localhost:5555/api/v1/customers"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']

def api_create_customer(name,email,address,phone,username,password):
    url = "http://localhost:5555/api/v1/customers"

    payload = {
        "name":name,
        "email":email,
        "address":address,
        "phone":phone,
        "username":username,
        "password":password
    }
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("POST", url, headers=headers, json = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['status']

#API_PRODUCT
def api_get_list_category():
    url = "http://localhost:5555/api/v1/products/categories"

    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    return result['result']
def api_get_category(id):
    url = "http://localhost:5555/api/v1/products/categories/" + str(id)
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    return result['result']


def api_get_list_products():
    url = "http://localhost:5555/api/v1/products"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']

def api_get_product(id):
    url = "http://localhost:5555/api/v1/products/" + str(id)

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']


def api_create_product(product_name,product_category,price,stock_price,quantity, description):
    url = "http://localhost:5555/api/v1/products"

    payload = {"product_name":product_name,
        "product_category":product_category,
        "price":price,
        "stock_price":stock_price,
        "quantity":quantity,
        "description":description}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_authentication()
    }

    response = requests.request("POST", url, headers=headers, json = payload)
    result = response.json()
    
    return result['status']

#API_ORDER
#API_ORDER'S DETAIL