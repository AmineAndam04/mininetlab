from mininet.topo import Topo
from mininet.link import TCIntf
from mininet.node import CPULimitedHost

class MyTopo( Topo,TCIntf,CPULimitedHost ):

    def build( self ):
        

        # Add hosts and switches
        leftHost = self.addHost( 'h1' , ip='10.0.0.1/24')
        rightHost = self.addHost( 'h2' , ip='10.0.0.2/24')
        Switch = self.addSwitch( 's1' )

        # Add links
        self.addLink( leftHost , Switch )
        self.addLink( rightHost, Switch , params1={'delay':'50ms', 'bw' : 10} )
        self.setCPUFrac(leftHost,0.2)


topos = { 'mytopo': ( lambda: MyTopo() ) }
