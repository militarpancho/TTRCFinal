from mininet.topo import Topo
from mininet.net import Mininet

class Anillo(Topo):

	def __init__(self, n1=13, n2=5 , n3=6):
		
		# Initialize topology
		Topo.__init__(self)
		
		self.host_number = 1
		self.switch_number = 1
		# Create Central Ring
		switchList = []
		switchList2 = []
		switchList3 = []
		access_switchList = []
		for swnum in range(n1):
			self.create_switch(switchList)
			if swnum > 0:
				self.addLink(switchList[swnum], switchList[swnum-1], bw=1000, delay='3ms')
			# Create lower aggregated ring
			if swnum == 1:
				self.create_customer(switchList, swnum)
				for swnum2 in range(n2):
					self.create_switch(switchList2)
					if swnum2 == 0:
						self.create_switch(access_switchList)
						self.addLink(switchList2[swnum2], access_switchList[swnum2], bw=1000, delay='3ms')
						self.create_customer(access_switchList, swnum2)
						self.create_customer(access_switchList, swnum2)
						self.addLink(switchList2[swnum2], switchList[swnum], bw=1000, delay='3ms')
					if swnum2 > 0:
						self.addLink(switchList2[swnum2], switchList2[swnum2-1], bw=1000, delay='3ms')
					if swnum2 == 1:
						self.create_customer(switchList2, swnum2)
					if swnum2 == 2:
						self.create_switch(access_switchList)
						self.addLink(switchList2[swnum2], access_switchList[swnum2-1], bw=1000, delay='3ms')
						self.create_customer(access_switchList, swnum2-1)
						self.create_customer(access_switchList, swnum2-1)
					if swnum2 == 3:
						self.create_customer(switchList2, swnum2)
			if swnum == 3:
				self.create_switch(access_switchList)
				self.addLink(switchList[swnum], access_switchList[swnum-1], bw=1000, delay='3ms')
				self.addLink(switchList[swnum], switchList2[n2-1], bw=1000, delay='3ms')
				self.create_customer(access_switchList, swnum-1)
				self.create_customer(access_switchList, swnum-1)
			if swnum == 4:
				self.create_switch(access_switchList)
				self.addLink(switchList[swnum], access_switchList[swnum-1], bw=1000, delay='3ms')
				self.create_customer(access_switchList, swnum-1)
				self.create_customer(access_switchList, swnum-1)
				self.create_customer(access_switchList, swnum-1)
			if swnum == 5:
				self.create_customer(switchList, swnum)
				self.create_customer(switchList, swnum)
			if swnum == 6:
				# Create upper aggregated Ring
				for swnum3 in range(n3):
					self.create_switch(switchList3)
					if swnum3 == 0:
						self.addLink(switchList3[swnum3], switchList[swnum], bw=1000, delay='3ms')
					if swnum3 > 0:
						self.addLink(switchList3[swnum3], switchList3[swnum3-1], bw=1000, delay='3ms')
					if swnum3 == 1:
						self.create_switch(access_switchList)
						self.addLink(switchList3[swnum3], access_switchList[-1], bw=1000, delay='3ms')
						self.create_switch(access_switchList)
						self.addLink(switchList3[swnum3], access_switchList[-1], bw=1000, delay='3ms')
						self.create_customer(access_switchList, -1)
						self.create_customer(access_switchList, -1)
						self.create_customer(access_switchList, -2)
					if swnum3 == 2:
						self.create_switch(access_switchList)
						self.addLink(switchList3[swnum3], access_switchList[-1], bw=1000, delay='3ms')
						self.create_customer(access_switchList, -1)
						self.create_customer(access_switchList, -1)
					if swnum3 == 3:
						self.create_switch(access_switchList)
						self.addLink(switchList3[swnum3], access_switchList[-1], bw=1000, delay='3ms')
						self.create_customer(access_switchList, -1)
						self.create_customer(switchList3, swnum3)
					if swnum3 == 4:
						self.create_switch(access_switchList)
						self.addLink(switchList3[swnum3], access_switchList[-1], bw=1000, delay='3ms')
						self.create_customer(switchList3, swnum3)
						self.create_customer(access_switchList, -1)
					if swnum3 == 5:
						self.create_customer(switchList3, swnum3)
			if swnum == 7:
				self.addLink(switchList[swnum], switchList3[n3-1], bw=1000, delay='3ms')
			if swnum == 8:
				self.create_customer(switchList, swnum)
			if swnum == 9:
				self.create_switch(access_switchList)
				self.addLink(switchList[swnum], access_switchList[-1], bw=1000, delay='3ms')
				self.create_customer(access_switchList, -1)
				self.create_customer(access_switchList, -1)
				self.create_customer(switchList, swnum)
			if swnum == 10:
				self.create_switch(access_switchList)
				self.addLink(switchList[swnum], access_switchList[-1], bw=1000, delay='3ms')
				self.create_customer(access_switchList, -1)
				self.create_customer(access_switchList, -1)
							
			if swnum == 11:
				self.create_customer(switchList, swnum)
				self.create_customer(switchList, swnum)
			if swnum == 12:
				self.create_switch(access_switchList)
				self.addLink(switchList[swnum], access_switchList[-1], bw=1000, delay='3ms')
				self.create_customer(access_switchList, -1)
				self.create_customer(access_switchList, -1)
				self.create_customer(access_switchList, -1)
				self.create_customer(switchList, swnum)
						
					
					
					

		self.addLink(switchList[0], switchList[n1-1], bw=1000, delay='3ms')
		
		
	
	def create_customer(self, slist, swnum):
		host = self.addHost('h%s' % (self.host_number))
		self.addLink(host, slist[swnum], bw=100, delay='2ms')
		self.host_number += 1

	def create_switch(self, switchList):
		switchList.append(self.addSwitch('sw%s' % (self.switch_number)))
		self.switch_number += 1

topos = { 'anillo': (lambda: Anillo())}
