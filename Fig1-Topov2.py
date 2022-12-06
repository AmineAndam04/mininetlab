from mininet.topo import Topo
class MyTopo( Topo ):

    def build( self ):
        

        # Add hosts and switches
        leftHost1 = self.addHost( 'h3' ,ip="10.0.1.2/24")
        leftHost2 = self.addHost( 'h4', ip="10.0.1.3/24" )
        rightHost = self.addHost( 'h5', ip="10.0.2.2/24" )
        leftSwitch = self.addSwitch( 's1' ,ip="10.0.1.1/24")
        rightSwitch = self.addSwitch( 's2', ip="10.0.2.1/24")

        # Add links
        self.addLink( leftHost1 , leftSwitch )
        self.addLink( leftHost2 , leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }