from vtnManager import ODLClient
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
    odl.create_vtnPortMap("sw8-eth2", "openflow:8", "if1", "vbr1", "hexagon")
    odl.create_vtnPortMap("sw14-eth2", "openflow:14", "if2", "vbr1", "hexagon")
    odl.create_vtnPortMap("sw27-eth2", "openflow:27", "if3", "vbr1", "hexagon")

    #Create Square VTN net (hss)
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
    odl.create_vtnPortMap("sw17-eth2", "openflow:17", "if3", "vbr2", "square")
    odl.create_vtnPortMap("sw20-eth2", "openflow:20", "if4", "vbr2", "square")
    odl.create_vtnPortMap("sw31-eth2", "openflow:31", "if5", "vbr2", "square")
    odl.create_vtnPortMap("sw33-eth2", "openflow:33", "if6", "vbr2", "square")
    odl.create_vtnPortMap("sw36-eth3", "openflow:36", "if7", "vbr2", "square")

    #Create Triangle VTN net (hts)
    odl = ODLClient("http://localhost:8181")
    odl.create_vtn("triangle")
    odl.create_vBridge("vbr3", "triangle")
    odl.create_vInterface("if1", "vbr3", "triangle")
    odl.create_vInterface("if2", "vbr3", "triangle")
    odl.create_vInterface("if3", "vbr3", "triangle")
    odl.create_vInterface("if4", "vbr3", "triangle")
    odl.create_vInterface("if5", "vbr3", "triangle")
    odl.create_vInterface("if6", "vbr3", "triangle")
    odl.create_vInterface("if7", "vbr3", "triangle")
    odl.create_vInterface("if8", "vbr3", "triangle")
    odl.create_vInterface("if9", "vbr3", "triangle")
    odl.create_vInterface("if10", "vbr3", "triangle")
    odl.create_vInterface("if11", "vbr3", "triangle")
    odl.create_vInterface("if12", "vbr3", "triangle")
    odl.create_vInterface("if13", "vbr3", "triangle")

    odl.create_vtnPortMap("sw3-eth1", "openflow:3", "if1", "vbr3", "triangle")
    odl.create_vtnPortMap("sw4-eth2", "openflow:4", "if2", "vbr3", "triangle")
    odl.create_vtnPortMap("sw5-eth2", "openflow:5", "if3", "vbr3", "triangle")
    odl.create_vtnPortMap("sw7-eth3", "openflow:7", "if4", "vbr3", "triangle")
    odl.create_vtnPortMap("sw12-eth3", "openflow:12", "if5", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw14-eth3", "openflow:14", "if6", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw22-eth2", "openflow:22", "if7", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw24-eth2", "openflow:24", "if8", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw25-eth3", "openflow:25", "if9", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw26-eth2", "openflow:26", "if10", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw31-eth3", "openflow:31", "if11", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw33-eth3", "openflow:33", "if12", "vbr3",
                          "triangle")
    odl.create_vtnPortMap("sw36-eth2", "openflow:36", "if13", "vbr3",
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
    hexagon_traffic = pickle.load(open("trafficset_hexagon.p", "rb"))
    for element in set(hexagon_traffic):
        hex_traffic_policy[element.replace("sw", "s")] = "10"
    response = odl.set_path_policy(hex_traffic_policy, "1", default_cost="1")
    logging.info(response)


def set_triangle_policy():
    odl = ODLClient("http://localhost:8181")
    square_traffic_policy = {}
    hexagon_traffic = set(
        pickle.load(open("vtnManager/trafficset_hexagon.p", "rb")))
    square_traffic = set(
        pickle.load(open("vtnManager/trafficset_square.p", "rb")))

    cost_15 = square_traffic & hexagon_traffic
    cost_10 = hexagon_traffic - square_traffic
    cost_5 = square_traffic - hexagon_traffic

    for element in set(cost_15):
        square_traffic_policy[element.replace("sw", "s")] = "15"

    for element in set(cost_10):
        square_traffic_policy[element.replace("sw", "s")] = "10"

    for element in set(cost_5):
        square_traffic_policy[element.replace("sw", "s")] = "5"

    response = odl.set_path_policy(
        square_traffic_policy, "2", default_cost="1")
    logging.info(response)


def set_path_map():
    odl = ODLClient("http://localhost:8181")
    for i in range(4, 11):
        response = odl.set_path_map("cond"+str(i), str(i), "1", "square")
        print(response)
    print("Flow Conditions for square hosts established")

    for i in range(11, 24):
        response = odl.set_path_map("cond"+str(i), str(i), "2", "triangle")
        print(response)
    print("Flow Conditions for square hosts established")


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
