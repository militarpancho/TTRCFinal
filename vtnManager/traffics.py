#!/bin/python
import pickle
import sys
import os
from vtnManager import ODLClient

odl = ODLClient("http://localhost:8181")


def get_traffic(vtn, traffic):
    ifaces = {
        "square": [
            "sw7-eth2", "sw12-eth2", "sw17-eth2", "sw20-eth2", "sw31-eth2",
            "sw33-eth2", "sw36-eth3"
        ],
        "hexagon": ["sw8-eth2", "sw14-eth2", "sw27-eth2"]
    }
    for iface in ifaces[vtn]:
        for dataflow in odl.get_dataflow(
                iface, "openflow:" + iface.split("-")[0].split("sw")[1], vtn):
            for phy in dataflow['physical-route']:
                traffic.append(phy['physical-egress-port']['port-name'])
                traffic.append(phy['physical-ingress-port']['port-name'])
    return traffic


if __name__ == "__main__":
    if os.path.isfile("traffic.p"):
        previous_traffic = pickle.load(open("traffic.p", "rb"))
    else:
        previous_traffic = []

    if len(sys.argv) == 3:
        if sys.argv[2] == "--set":
            print(list(set(previous_traffic)))
            pickle.dump(
                list(set(previous_traffic)),
                open("trafficset_" + sys.argv[1] + ".p", "wb"))
            os.remove("traffic.p")
    else:
        pickle.dump(
            get_traffic(sys.argv[1], previous_traffic), open(
                "traffic.p", "wb"))
        print("Saving traffic data...Please, repeat during pingall " +
              sys.argv[1] + " hosts. When finish, add --set flag")
