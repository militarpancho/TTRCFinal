
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


# In[98]:


#Create Hexagon VTN net (h7, h11 y h27)
odl = ODLClient("http://localhost:8181")
odl.create_vtn("hexagon")
odl.create_vBridge("vbr1", "hexagon")
odl.create_vInterface("if1", "vbr1", "hexagon")
odl.create_vInterface("if2", "vbr1", "hexagon")
odl.create_vInterface("if3", "vbr1", "hexagon")
odl.create_vtnPortMap("sw8-eth2", "openflow:8", "if1", "vbr1", "hexagon")
odl.create_vtnPortMap("sw14-eth3", "openflow:14", "if2", "vbr1", "hexagon")
odl.create_vtnPortMap("sw27-eth2", "openflow:27", "if3", "vbr1", "hexagon")


# In[99]:


#Create Square VTN net (h5,h8,h2,h18,h27,h30,h34)
odl = ODLClient("http://localhost:8181")
odl.create_vtn("square")
odl.create_vBridge("vbr2", "square")
odl.create_vInterface("if1", "vbr2", "square")
odl.create_vInterface("if2", "vbr2", "square")
odl.create_vInterface("if3", "vbr2", "square")
odl.create_vInterface("if4", "vbr2", "square")
odl.create_vInterface("if5", "vbr2", "square")
odl.create_vInterface("if6", "vbr2", "square")
odl.create_vInterface("if7", "vbr2", "square")

odl.create_vtnPortMap("sw7-eth2", "openflow:7", "if1", "vbr2", "square")
odl.create_vtnPortMap("sw12-eth2", "openflow:12", "if2", "vbr2", "square")
odl.create_vtnPortMap("sw4-eth2", "openflow:4", "if3", "vbr2", "square")
odl.create_vtnPortMap("sw19-eth2", "openflow:19", "if4", "vbr2", "square")
odl.create_vtnPortMap("sw31-eth2", "openflow:31", "if5", "vbr2", "square")
odl.create_vtnPortMap("sw33-eth2", "openflow:33", "if6", "vbr2", "square")
odl.create_vtnPortMap("sw36-eth2", "openflow:36", "if7", "vbr2", "square")


# In[100]:


odl = ODLClient("http://localhost:8181")
odl.get_vtns()

