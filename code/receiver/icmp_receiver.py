#!/usr/bin/env python3
from scapy.all import sniff, IP, ICMP

def callback(packet):
    """
    Callback function to execute when received packets
    """
    if IP in packet and ICMP in packet:
        # Only show ICMP requests with TTL=1
        if packet[ICMP].type == 8 and packet[IP].ttl == 1:
            print("\nReceived ICMP packet from:", packet[IP].src)
            packet.show()

def start_receiver():

    try:
        sniff(filter="icmp", prn=callback)
    except KeyboardInterrupt:
        print("\nStopping receiver...")

# Comment out for Sphinx documentation
'''
if __name__ == "__main__":
    start_receiver()
'''
