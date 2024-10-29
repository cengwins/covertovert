import scapy.all as scapy

# set constants
TTL = 1
DESTINATION = 'receiver'

NUM_OF_PACKET = 1

def send_packet():
    # create the packet
    packet = scapy.IP(
        dst = DESTINATION,
        ttl = TTL
    )

    # make packet icmp
    packet = packet / scapy.ICMP()

    # send packet
    scapy.send(packet, verbose=False)

def main():
    for _ in range(NUM_OF_PACKET):
        send_packet()
    

if __name__ == '__main__':
    main()
