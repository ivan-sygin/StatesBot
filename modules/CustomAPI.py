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

    def __init__(self, protocol, ip, port, path_token):
        self.protocol = protocol
        self.ip = ip
        self.port = port
        self.path_token = path_token

    def updateUrl(self):
        self.url = self.protocol + "://" + self.ip + ":" + self.port

    def fetchGetJson(self, api_path: str, auth=True, data=None) -> dict:
        url = self.url + api_path
        params = data

        if auth:
            params['token'] = os.environ[self.path_token]

        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise generateException(response.status_code, 'fetchGetJson', response.request)

        return response.json()

    def fetchGetNoResponse(self, api_path: str, auth=True, data=None):
        url = self.url + api_path
        params = data

        if auth:
            params['token'] = os.environ[self.path_token]

        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise generateException(response.status_code, 'fetchGetNoResponse', response.request)

        return response.status_code
