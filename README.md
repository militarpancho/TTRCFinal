# Install neccesary features in opendaylight
'''
$ docker exec -ti opendaylight bash
$ cd distribution-...
$ bin/client

Install this features first in odl:
feature:install odl-mdsal-clustering
feature:install odl-restconf
feature:install odl-mdsal-apidocs
feature:install odl-vtn-manager
feature:install odl-dlux-core
feature:install odl-dlux-all

'''
# Run mininet topology 

'''
sudo mn --mac --custom=arbitraria.py --topo anillo --link tc --controller remote,ip=172.20.0.2 --switch ovsk
'''


# Dudas

- Cada red vtn tiene un vBridge o varios.