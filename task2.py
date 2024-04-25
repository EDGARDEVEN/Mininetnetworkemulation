from mininet.node import Host
from mininetwifi.mn_wifi.node import Station
from mininetwifi.mn_wifi import link
from mininet.cli import CLI

# Define network parameters (modify these based on your assignment)
num_stations = 3  # Number of stations in the ad hoc network
ssid = 'adhoc_network'  # Service Set Identifier
channel = 1  # Wireless channel

# Define device configurations (replace with data from your table)
import mininet.net

sta_macs = ['00:00:00:00:00:01', '00:00:00:00:00:02', '00:00:00:00:00:03']
sta_ips = ['10.0.0.1', '10.0.0.2', '10.0.0.3']

# Create Mininet network
net = mininet.net.Mininet(waitConn=True)

# Create stations (modify for additional configurations)
stations = []
for i in range(num_stations):
    sta = Station(f'sta{i+1}', mac=sta_macs[i], ip=sta_ips[i], ssid=ssid, channel=channel)
    stations.append(sta)
    net.addNode(sta)

# Uncomment the following line to enable mobility (modify parameters)
# net.mobility(pop=stations, ac='', limit=False, time=0, startMobility=False)

# Create links between stations (optional)
# Link(sta1, sta2)  # Replace sta1 and sta2 with actual stations

# Start the network
net.start()

# You can now configure routing protocols, initiate traffic, and collect data
# Refer to the assignment instructions and resources mentioned previously

# Stop the network
net.stop()

print("Network stopped")
