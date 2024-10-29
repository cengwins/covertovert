#!/usr/bin/env python3
from scapy.all import IP, ICMP, send, conf

def create_and_send_icmp_packet(dst_ip):
    """
    Creates and sends an ICMP packet with TTL=1 to the specified destination.
    """
    try:
        # Disable verbose output
        conf.verb = 0
        
        # Create IP packet with TTL=1 and correct source IP
        ip_packet = IP(src="172.18.0.2", dst=dst_ip, ttl=1)  # Updated sender IP
        
        # Create ICMP echo request packet
        icmp_packet = ICMP(type=8, code=0)
        
        # Combine the packets
        packet = ip_packet/icmp_packet
        
        print("Sending ICMP packet to receiver...")
        send(packet)
        print("Packet sent successfully")
        
    except Exception as e:
        print(f"Error sending packet: {e}")

if __name__ == "__main__":
    RECEIVER_IP = "172.18.0.3"  # Updated receiver IP
    create_and_send_icmp_packet(RECEIVER_IP)