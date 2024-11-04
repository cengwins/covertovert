import scapy.all as scapy 

def handle_packet(packet):
    if scapy.ICMP in packet and packet[scapy.IP].ttl == 1:
        #Captured an ICMP packet
        packet.show()

scapy.sniff(filter="icmp", prn=handle_packet, count=1)

