from CovertChannelBase import CovertChannelBase
from scapy.all import IP, UDP, DNS
import random
import time

class MyCovertChannel(CovertChannelBase):
    """
    - You are not allowed to change the file name and class name.
    - You can edit the class in any way you want (e.g. adding helper functions); however, there must be a "send" and a "receive" function, the covert channel will be triggered by calling these functions.
    """
    def __init__(self):
        """
        - You can edit __init__.
        """
        pass
    def send(self, log_file_name, parameter1, parameter2):
        """
        - In this function, you expected to create a random message (using function/s in CovertChannelBase), and send it to the receiver container. Entire sending operations should be handled in this function.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """

        # The actual message that will be sent through covert channel
        binary_message = self.generate_random_binary_message_with_logging(log_file_name)

        # Defining XOR
        bitIsZero = ["00", "11"]
        bitIsOne = ["01", "10"]


        length = len(binary_message)
        i = 0

        # Looping over the data to send
        while i < length:

            ## First processing first bit
            # If first bit to send is 0, rcode's left side two bits, when xor'ed, will equal 0
            if binary_message[i] == "0":
                rcode = random.choice(bitIsZero)

            # Else first bit to send is 1, rcode's left side two bits, when xor'ed, will equal 1
            else:
                rcode += random.choice(bitIsOne)

            i += 1

            # Now sending the packet

            packet = IP(dst = "receiver")/UDP()/DNS(
            qr = 1, # seting to 1 for response to avoid detection
            rcode = int(rcode, 2)   # embedding 2 bits of data here
            )

            super().send(packet)
            time.sleep(0.01)
        
    def receive(self, parameter1, parameter2, parameter3, log_file_name):
        """
        - In this function, you are expected to receive and decode the transferred message. Because there are many types of covert channels, the receiver implementation depends on the chosen covert channel type, and you may not need to use the functions in CovertChannelBase.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """
        self.log_message("", log_file_name)
