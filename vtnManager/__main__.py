from vtnManager import ODLClient
import pickle
import logging
import sys
import os

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
	odl.create_vtnPortMap("sw12-eth3", "openflow:12", "if5", "vbr3", "triangle")
	odl.create_vtnPortMap("sw14-eth3", "openflow:14", "if6", "vbr3", "triangle")
	odl.create_vtnPortMap("sw22-eth2", "openflow:22", "if7", "vbr3", "triangle")
	odl.create_vtnPortMap("sw24-eth2", "openflow:24", "if8", "vbr3", "triangle")
	odl.create_vtnPortMap("sw25-eth3", "openflow:25", "if9", "vbr3", "triangle")
	odl.create_vtnPortMap("sw26-eth2", "openflow:26", "if10", "vbr3", "triangle")
	odl.create_vtnPortMap("sw31-eth3", "openflow:31", "if11", "vbr3", "triangle")
	odl.create_vtnPortMap("sw33-eth3", "openflow:33", "if12", "vbr3", "triangle")
	odl.create_vtnPortMap("sw36-eth2", "openflow:36", "if13", "vbr3", "triangle")
        
	print("VTNs created and configured")
        
def set_flow_conditions():
	odl = ODLClient("http://localhost:8181")
	for i in range(11,23):
		odl.set_flow_cond("cond"+str(i), str(i), "10.0.0."+str(i), "10.0.0."+str(i+1))
		odl.set_flow_cond("cond"+str(i+12), str(i+12), "10.0.0."+str(i+1), "10.0.0."+str(i))
		if (i+2) <= 23:
			odl.set_flow_cond("cond"+str(i+24), str(i+24), "10.0.0."+str(i), "10.0.0."+str(i+2))
			odl.set_flow_cond("cond"+str(i+35), str(i+35), "10.0.0."+str(i+2), "10.0.0."+str(i))
		if (i+3) <= 23:
			odl.set_flow_cond("cond"+str(i+46), str(i+46), "10.0.0."+str(i), "10.0.0."+str(i+3))
			odl.set_flow_cond("cond"+str(i+56), str(i+56), "10.0.0."+str(i+3), "10.0.0."+str(i))
		if (i+4) <= 23:
			odl.set_flow_cond("cond"+str(i+66), str(i+66), "10.0.0."+str(i), "10.0.0."+str(i+4))
			odl.set_flow_cond("cond"+str(i+74), str(i+74), "10.0.0."+str(i+4), "10.0.0."+str(i))
		if (i+5) <= 23:
			odl.set_flow_cond("cond"+str(i+82), str(i+82), "10.0.0."+str(i), "10.0.0."+str(i+5))
			odl.set_flow_cond("cond"+str(i+90), str(i+90), "10.0.0."+str(i+5), "10.0.0."+str(i))
		if (i+6) <= 23:
			odl.set_flow_cond("cond"+str(i+98), str(i+98), "10.0.0."+str(i), "10.0.0."+str(i+6))
			odl.set_flow_cond("cond"+str(i+105), str(i+105), "10.0.0."+str(i+6), "10.0.0."+str(i))
		if (i+7) <= 23:
			odl.set_flow_cond("cond"+str(i+112), str(i+112), "10.0.0."+str(i), "10.0.0."+str(i+7))
			odl.set_flow_cond("cond"+str(i+118), str(i+118), "10.0.0."+str(i+7), "10.0.0."+str(i))
		if (i+8) <= 23:
			odl.set_flow_cond("cond"+str(i+123), str(i+123), "10.0.0."+str(i), "10.0.0."+str(i+8))
			odl.set_flow_cond("cond"+str(i+127), str(i+127), "10.0.0."+str(i+8), "10.0.0."+str(i))
		if (i+9) <= 23:
			odl.set_flow_cond("cond"+str(i+132), str(i+132), "10.0.0."+str(i), "10.0.0."+str(i+9))
			odl.set_flow_cond("cond"+str(i+136), str(i+136), "10.0.0."+str(i+9), "10.0.0."+str(i))
		if (i+10) <= 23:
			odl.set_flow_cond("cond"+str(i+140), str(i+140), "10.0.0."+str(i), "10.0.0."+str(i+10))
			odl.set_flow_cond("cond"+str(i+143), str(i+143), "10.0.0."+str(i+10), "10.0.0."+str(i))
		if (i+11) <= 23:
			odl.set_flow_cond("cond"+str(i+146), str(i+146), "10.0.0."+str(i), "10.0.0."+str(i+11))
			odl.set_flow_cond("cond"+str(i+148), str(i+148), "10.0.0."+str(i+11), "10.0.0."+str(i))
		if (i+12) <= 23:
			odl.set_flow_cond("cond"+str(i+150), str(i+150), "10.0.0."+str(i), "10.0.0."+str(i+12))
			odl.set_flow_cond("cond"+str(i+151), str(i+151), "10.0.0."+str(i+12), "10.0.0."+str(i))


def set_square_policy():
	odl = ODLClient("http://localhost:8181")
	hex_traffic_policy = {}
	hexagon_traffic = pickle.load( open( "trafficset_hexagon.p", "rb" ))
	for element in set(hexagon_traffic):
    	hex_traffic_policy[element.replace("sw", "s")] = "10"
    odl.set_path_policy(hex_trafic_policy, "1", default_cost="1")

def set_triangle_policy():
	odl = ODLClient("http://localhost:8181")
	square_traffic_policy = {}
	hexagon_traffic = set(pickle.load( open( "vtnManager/trafficset_hexagon.p", "rb" )))
	square_traffic = set(pickle.load( open( "vtnManager/trafficset_square.p", "rb" )))

	cost_15 = square_traffic & hexagon_traffic 
	cost_10 = hexagon_traffic - square_traffic
	cost_5 = square_traffic - hexagon_traffic

	for element in set(cost_15):
    	square_traffic_policy[element.replace("sw", "s")] = "15"

    for element in set(cost_10):
    	square_traffic_policy[element.replace("sw", "s")] = "10"

    for element in set(cost_5):
    	square_traffic_policy[element.replace("sw", "s")] = "5"

    odl.set_path_policy(square_traffic_policy, "2", default_cost="1")

def set_path_map():
	odl = ODLClient("http://localhost:8181")
	print("Not implemented yet")

if __name__ == "__main__":
	if sys.argv[1] == "create_vtns":
		vtns()
	elif sys.argv[2] == "set_flow_conditions":
		set_flow_conditions()
	elif sys.argv[3] == "set_path_policies":
		if os.path.isfile("trafficset_hexagon"):
			set_square_policy()
		else:
			print("Please, get traffics from hexagon vtn first using 'python traffics.py hexagon' during pingall hexagon hosts in mininet")
		if os.path.isfile("trafficset_square"):
			set_triangle_policy()
		else:
			print("Please, get traffics from square vtn first using 'python traffics.py square' during pingall square hosts in mininet")
	elif sys.argv[3] == "set_path_map":
		set_path_map()
