import os
import sys
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.examples import mobility
from mininetwifi.mn_wifi.node import Station



# Define network parameters
num_stations = 5  # Number of stations (laptops/smartphones)

# Get user input for access point details (replace with actual values)
num_aps = int(input("Enter the total number of access points (including those for lecture rooms): "))
ap_locations = []
ap_ssids = []
ap_passwords = []
ap_channels = []
for i in range(num_aps):
    location = input(f"Enter location for access point {i+1}: ")
    ssid = input(f"Enter SSID for access point {i+1}: ")
    password = input(f"Enter password for access point {i+1}: ")
    channel = int(input(f"Enter channel (1-11) for access point {i+1}: "))
    ap_locations.append(location)
    ap_ssids.append(ssid)
    ap_passwords.append(password)
    ap_channels.append(channel)

# Create Mininet objects
net = Mininet(controller=Controller, switch=OVSKernelSwitch)

# Create stations
stations = [ Station(f'sta{i}') for i in range(num_stations) ]
for sta in stations:
    net.addNode(sta)

# Create access points based on user input
access_points = []
for i, (loc, ssid, pwd, chan) in enumerate(zip(ap_locations, ap_ssids, ap_passwords, ap_channels)):
    ap = net.addAccessPoint('ap{}'.format(i+1), ssid=ssid, passwd=pwd, channel=chan, mode='g', range=35)  # Adjust mode and range if needed
    access_points.append(ap)

# Define mobility model parameters (adjust as needed)
max_x = 100  # Maximum X coordinate for movement (adjust based on floor plan)
max_y = 100  # Maximum Y coordinate for movement (adjust based on floor plan)
min_v = 0.1   # Minimum speed (meters per second)
max_v = 1.0   # Maximum speed (meters per second)
seed = 20     # Seed for random movement (change for different behavior)

# Enable mobility for stations
for sta in stations:
    mobility(net, sta, model='RandomDirection', max_x=max_x, max_y=max_y, min_v=min_v, max_v=max_v, seed=seed)

# Start the network
net.build()
net.start()

# Run CLI for user interaction
CLI(net)

# Stop the network
net.stop()
