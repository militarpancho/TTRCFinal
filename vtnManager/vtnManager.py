
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
    
    def get_dataflow(self, vtnPortMap, node, vtnName, **params):
        data = {"input":{"tenant-name": vtnName,
                         "data-flow-port": {"port-name": vtnPortMap, "port-id": vtnPortMap[-1]},
                         "node": node,
                         "mode": "DETAIL",
                         }}
        path = "/operations/vtn-flow:get-data-flow"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()['output']['data-flow-info']

        except:
            return response.text        


    def set_flow_cond(self, cond, index, ipsource, ipdestination, **params):
        data = {"input":{"operation":"SET",
                         "present":"false",
                         "name":cond, 
                         "vtn-flow-match":[{"vtn-ether-match":{},
                                            "vtn-inet-match":{"source-network":ipsource+"/32",
                                                              "protocol":1,
                                                              "destination-network":ipdestination+"/32"},
                                                              "index":index}
                                            ]
                        }
                }
        path = "/operations/vtn-flow-condition:set-flow-condition"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text

    def set_path_map(self, cond, index, policy, vtnName, **params):
        data = {"input":{"tenant-name": vtnName,
                         "path-map-list":[{"condition":cond,
                                           "policy":policy,
                                           "index": index,
                                           "idle-timeout":"300",
                                           "hard-timeout":"0"}]}}
        path = "/operations/vtn-path-map:set-path-map"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text 

    def set_path_policy(self, vtn_path_cost, policy,  default_cost=1,  **params):
        data = {"input":{"operation":"SET",
                         "id": policy,
                         "default-cost": default_cost,
                         "vtn-path-cost": []
                        }
                }
        for element in vtn_path_cost:
            data['input']['vtn-path-cost'].append({"port-desc":"openflow:"+element.split("-")[0].split("s")[1]+","+element[-1]+","+element,
                                            "cost":vtn_path_cost[element]})
        path = "/operations/vtn-path-policy:set-path-policy"
        url = '{}{}'.format(self.endpoint, path)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=params, data=json.dumps(data), auth=self.auth,headers=headers)
        try:
            return response.json()
        except:
            return response.text 
