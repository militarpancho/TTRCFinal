from vtnManager import ODLClient


def main():
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
        


if __name__ == "__main__":
	main()
