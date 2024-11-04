import scapy.all as scapy

# Implement your ICMP sender here

receiver_ip = "172.19.0.3"

packet = scapy.IP(dst=receiver_ip, ttl=1) / scapy.ICMP()

scapy.send(packet)
#Sent ICMP packet to receiver
