import scapy.all as scapy

# set constants
NUM_OF_PACKET = 1

def check_and_show_packet(packet):
    # check for icmp layer and ttl 
    if not packet.haslayer(scapy.ICMP):
        return
    
    if packet[scapy.IP].ttl != 1:
        return
    
    # show packet if it is an ICMP packet and TTL value is 1
    packet.show()

def main():
    # wait for packet
    scapy.sniff(
        filter = 'icmp',
        prn = check_and_show_packet,
        count = NUM_OF_PACKET
    )

if __name__ == '__main__':
    main()