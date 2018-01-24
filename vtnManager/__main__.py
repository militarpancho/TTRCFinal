from .vtnManager import ODLClient
import pickle
import logging
import sys
import os
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def vtns():
    #Create Hexagon VTN net (hhs)
    odl = ODLClient("http://localhost:8181")
    odl.create_vtn("hexagon")
    odl.create_vBridge("vbr1", "hexagon")
    odl.create_vInterface("if1", "vbr1", "hexagon")
    odl.create_vInterface("if2", "vbr1", "hexagon")
    odl.create_vInterface("if3", "vbr1", "hexagon")
    odl.create_vtnPortMap("s8-eth2", "openflow:8", "if1", "vbr1", "hexagon")
    odl.create_vtnPortMap("s14-eth2", "openflow:14", "if2", "vbr1", "hexagon")
    odl.create_vtnPortMap("s27-eth2", "openflow:27", "if3", "vbr1", "hexagon")

    #Create Square VTN net (hss)
    odl = ODLClient("http://localhost:8181")
    odl.create_vtn("square")
    odl.create_vBridge("vbr1", "square")
    odl.create_vInterface("if1", "vbr1", "square")
    odl.create_vInterface("if2", "vbr1", "square")
    odl.create_vInterface("if3", "vbr1", "square")
    odl.create_vInterface("if4", "vbr1", "square")
    odl.create_vInterface("if5", "vbr1", "square")
    odl.create_vInterface("if6", "vbr1", "square")
    odl.create_vInterface("if7", "vbr1", "square")

    odl.create_vtnPortMap("s7-eth2", "openflow:7", "if1", "vbr1", "square")
    odl.create_vtnPortMap("s12-eth2", "openflow:12", "if2", "vbr1", "square")
    odl.create_vtnPortMap("s17-eth2", "openflow:17", "if3", "vbr1", "square")
    odl.create_vtnPortMap("s20-eth2", "openflow:20", "if4", "vbr1", "square")
    odl.create_vtnPortMap("s31-eth2", "openflow:31", "if5", "vbr1", "square")
    odl.create_vtnPortMap("s33-eth2", "openflow:33", "if6", "vbr1", "square")
    odl.create_vtnPortMap("s36-eth3", "openflow:36", "if7", "vbr1", "square")

    #Create Triangle VTN net (hts)
    odl = ODLClient("http://localhost:8181")
    odl.create_vtn("triangle")
    odl.create_vBridge("vbr1", "triangle")
    odl.create_vInterface("if1", "vbr1", "triangle")
    odl.create_vInterface("if2", "vbr1", "triangle")
    odl.create_vInterface("if3", "vbr1", "triangle")
    odl.create_vInterface("if4", "vbr1", "triangle")
    odl.create_vInterface("if5", "vbr1", "triangle")
    odl.create_vInterface("if6", "vbr1", "triangle")
    odl.create_vInterface("if7", "vbr1", "triangle")
    odl.create_vInterface("if8", "vbr1", "triangle")
    odl.create_vInterface("if9", "vbr1", "triangle")
    odl.create_vInterface("if10", "vbr1", "triangle")
    odl.create_vInterface("if11", "vbr1", "triangle")
    odl.create_vInterface("if12", "vbr1", "triangle")
    odl.create_vInterface("if13", "vbr1", "triangle")

    odl.create_vtnPortMap("s3-eth1", "openflow:3", "if1", "vbr1", "triangle")
    odl.create_vtnPortMap("s4-eth2", "openflow:4", "if2", "vbr1", "triangle")
    odl.create_vtnPortMap("s5-eth2", "openflow:5", "if3", "vbr1", "triangle")
    odl.create_vtnPortMap("s7-eth3", "openflow:7", "if4", "vbr1", "triangle")
    odl.create_vtnPortMap("s12-eth3", "openflow:12", "if5", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s14-eth3", "openflow:14", "if6", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s22-eth2", "openflow:22", "if7", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s24-eth2", "openflow:24", "if8", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s25-eth3", "openflow:25", "if9", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s26-eth2", "openflow:26", "if10", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s31-eth3", "openflow:31", "if11", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s33-eth3", "openflow:33", "if12", "vbr1",
                          "triangle")
    odl.create_vtnPortMap("s36-eth2", "openflow:36", "if13", "vbr1",
                          "triangle")

    print("VTNs created and configured")


def set_flow_conditions():
    odl = ODLClient("http://localhost:8181")
    for i in range(4, 24):
        print("10.0.0." + str(i))
        odl.set_flow_cond("cond" + str(i), str(i), "10.0.0." + str(i))
    print("Flow Conditions for hosts established")


def set_square_policy():
    odl = ODLClient("http://localhost:8181")
    hex_traffic_policy = {}
    local_path = os.path.dirname(os.path.abspath(__file__))
    hexagon_traffic = pickle.load(open(local_path+"/trafficset_hexagon.p", "rb"))
    for element in set(hexagon_traffic):
        hex_traffic_policy[element] = "10"
    response = odl.set_path_policy(hex_traffic_policy, "1", default_cost="1")
    logging.info(response)


def set_triangle_policy():
    odl = ODLClient("http://localhost:8181")
    square_traffic_policy = {}
    local_path = os.path.dirname(os.path.abspath(__file__))
    hexagon_traffic = set(
        pickle.load(open(local_path+"/trafficset_hexagon.p", "rb")))
    square_traffic = set(
        pickle.load(open(local_path+"/trafficset_square.p", "rb")))

    cost_15 = square_traffic & hexagon_traffic
    cost_10 = hexagon_traffic - square_traffic
    cost_5 = square_traffic - hexagon_traffic

    for element in set(cost_15):
        square_traffic_policy[element] = "15"

    for element in set(cost_10):
        square_traffic_policy[element] = "10"

    for element in set(cost_5):
        square_traffic_policy[element] = "5"

    response = odl.set_path_policy(
        square_traffic_policy, "2", default_cost="1")
    logging.info(response)


def set_path_map():
    odl = ODLClient("http://localhost:8181")
    for i in range(4, 11):
        response = odl.set_path_map("cond"+str(i), str(i), "1", "square")
        print(response)
    print("Path maps for square hosts established")

    for i in range(11, 24):
        response = odl.set_path_map("cond"+str(i), str(i), "2", "triangle")
        print(response)
    print("Path maps for triangle hosts established")


if __name__ == "__main__":
    local_path = os.path.dirname(os.path.abspath(__file__))
    if sys.argv[1] == "create_vtns":
        vtns()
    elif sys.argv[1] == "set_flow_conditions":
        set_flow_conditions()
    elif sys.argv[1] == "set_path_policies":
        if os.path.isfile(local_path + "/trafficset_hexagon.p"):
            set_square_policy()
        else:
            print(
                "Please, get traffics from hexagon vtn first using 'python traffics.py hexagon' during pingall hexagon hosts in mininet"
            )
        if os.path.isfile(local_path + "/trafficset_square.p"):
            set_triangle_policy()
        else:
            print(
                "Please, get traffics from square vtn first using 'python traffics.py square' during pingall square hosts in mininet"
            )
    elif sys.argv[1] == "set_path_map":
        set_path_map()

    elif sys.argv[1] == "clean":
        odl = ODLClient("http://localhost:8181")
        if 'vtn-flow-condition' in odl.get_flow_conds()['vtn-flow-conditions']:
            for element in odl.get_flow_conds()['vtn-flow-conditions']['vtn-flow-condition']:
                odl.remove_flow_cond(element['name'])
                print(element["name"] + " deleted")
        if 'vtn' in odl.get_vtns()['vtns']:
            for element in odl.get_vtns()["vtns"]["vtn"]:
                odl.delete_vtn(element["name"])
                print(element["name"] + " deleted")
        if 'vtn-path-policy' in odl.get_path_policies()['vtn-path-policies']:
            for element in odl.get_path_policies()["vtn-path-policies"]["vtn-path-policy"]:
                odl.remove_path_policy(element["id"])
                print(str(element["id"]) + " deleted")

    elif sys.argv[1] == "get_dataflow_route":
        odl = ODLClient("http://localhost:8181")
        for route in odl.get_dataflow_route(sys.argv[2], sys.argv[3], sys.argv[4])[-1]["physical-route"]:
            print(route["node"])

