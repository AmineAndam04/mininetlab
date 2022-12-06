

from mininet.topo import Topo

class MyTopo( Topo ):

    def build( self ):
        

        # Add hosts and switches
        leftHost1 = self.addHost( 'h3' )
        leftHost2 = self.addHost( 'h4' )
        rightHost = self.addHost( 'h5' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost1 , leftSwitch )
        self.addLink( leftHost2 , leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }