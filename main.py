from vtnManager import ODLClient


def main():
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

if __main__ == "__name__":
	main()