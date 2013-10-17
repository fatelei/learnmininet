#!/usr/bin/python
#-*-coding: utf8-*-

"""
    topology

    host ------- switch ------- switch ------- host 

"""


from mininet.topo import Topo


class MyTopo(Topo):

    def __init__(self):
        Topo.__init__(self)

        # add hosts and switches
        leftHost = self.addHost("h1")
        rightHost = self.addHost("h2")
        leftSwitch = self.addSwitch("s3")
        rightSwitch = self.addSwitch("s4")

        # add links
        self.addLink(leftHost, leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightSwitch, rightHost)

topos = {"mytopo": (lambda: MyTopo())}
