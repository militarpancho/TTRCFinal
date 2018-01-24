# Install neccesary features in opendaylight

```bash
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
```

# Run mininet topology 

```bash
$ docker exec -ti mininet bash

sudo mn --mac --custom=arbitraria.py --topo anillo --link tc --controller remote,ip=172.20.0.2 --switch ovsk
```


#Run VTNs

```bash
$ cd TTRCFinal
$ python -m vtnManager create_vtns
$ python -m vtnManager set_flow_conditions
$ python -m vtnManager set_path_map
$ python -m vtnManager set_path_policy
```
# Get traffic data

# Verificate creation
```python
odl.get_dataflow("s7-eth2", "openflow:7","square")
```
*** This could be sloooow


# Questions


