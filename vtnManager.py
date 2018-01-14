
import requests
import logging
import json

class ODLClient(object):
    def __init__(self, endpoint, credentials=('admin', 'admin')):
        if endpoint[-1] == '/':
        endpoint = endpoint[0:-1]
        self.endpoint = '{}{}'.format(endpoint, '/restconf')
        self.credentials = credentials
        self.auth = (credentials[0], credentials[1])
    
    def request(self, path=None, method='GET', **params):
        url = '{}{}'.format(self.endpoint, path)
        response = requests.request(
            method=method, url=url, params=params, auth=self.auth)
        try:
            return response.json()
        except:
            return response.text
    def get_vtns(self, **params):
        path = "/operational/vtn:vtns"
        url = '{}{}'.format(self.endpoint, path)
        response = requests.get(url, params=params, auth=self.auth)
        try:
            return response.json()
        except:
            return response.text
    
    def create_vtn(self, name, **params):
        data = {"input":{"tenant-name": name}}
        path = "/operations/vtn:update-vtn"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text
   
    def delete_vtn(self, name, **params):
        data = {"input":{"tenant-name": name}}
        path = "/operations/vtn:remove-vtn"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text

    def create_vBridge(self, vBridgeName, vtnName, **params):
        data = {"input":{"tenant-name": vtnName, "bridge-name":vBridgeName}}
        path = "/operations/vtn-vbridge:update-vbridge"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text
    
    def create_vInterface(self, vInterfaceName, vBridgeName, vtnName, **params):
        data = {"input":{"tenant-name": vtnName, "bridge-name":vBridgeName, "interface-name": vInterfaceName}}
        path = "/operations/vtn-vinterface:update-vinterface"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text
    
    def create_vtnPortMap(self, vtnPortMap, node, vInterfaceName, vBridgeName, vtnName, **params):
        data = {"input":{"tenant-name": vtnName, 
                         "bridge-name":vBridgeName, 
                         "interface-name": vInterfaceName,
                         "node": node,
                         "port-name": vtnPortMap}}
        path = "/operations/vtn-port-map:set-port-map"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text
