import os

import requests


class MyException(Exception):
    pass


def generateException(statusCode, function, request):
    return MyException({
        'module': 'CustomAPI',
        'statusCode': statusCode,
        'function': 'fetchGetNoResponse',
        'request': request
    })


class API_Handler:
    protocol = 'https'
    ip = '26.'
    port = '8000'
    url = ''
    path_token = ''
    auth_type = ''

    def __init__(self, protocol, ip, port, path_token=None):
        self.protocol = protocol
        self.ip = ip
        self.port = port
        self.path_token = path_token

    def updateUrl(self):
        self.url = self.protocol + "://" + self.ip + ":" + self.port

    def fetchGetJson(self, api_path: str, auth_type='none', data=None) -> dict:
        url = self.url + api_path
        headers = {}
        params = data

        if auth_type == 'get':
            params['token'] = os.environ[self.path_token]
        elif auth_type == 'bearer':
            headers['Authorization'] = 'Bearer ' + os.environ[self.path_token]

        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            raise generateException(response.status_code, 'fetchGetJson', response.request)

        return response.json()

    def fetchGetNoResponse(self, api_path: str, auth_type='none', data=None):
        url = self.url + api_path
        headers = {}
        params = data

        if auth_type == 'get':
            params['token'] = os.environ[self.path_token]
        elif auth_type == 'bearer':
            headers['Authorization'] = 'Bearer ' + os.environ[self.path_token]

        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise generateException(response.status_code, 'fetchGetNoResponse', response.request)

        return response.status_code

    def fetchPostJson(self, api_path: str, auth_type='none', data=None) -> dict:
        url = self.url + api_path
        headers = {}
        payload = {}
        json = data

        if auth_type == 'get':
            payload['token'] = os.environ[self.path_token]
        elif auth_type == 'json':
            json['token'] = os.environ[self.path_token]
        elif auth_type == 'bearer':
            headers['Authorization'] = 'Bearer ' + os.environ[self.path_token]

        response = requests.post(url, json=json, headers=headers, params=payload)

        if response.status_code != 200:
            raise generateException(response.status_code, 'fetchGetJson', response.request)

        return response.json()
