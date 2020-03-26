def is_better(BPDU1, BPDU2):
    # If root is greater than BPDU1 is better
    if (BPDU1[0] < BPDU2[0]):
        return 1
    elif (BPDU1[0] == BPDU2[0] and BPDU1[1] < BPDU2[1]):
        return 1
    elif (BPDU1[0] == BPDU2[0] and BPDU1[1] == BPDU2[1] and BPDU1[2] < BPDU2[2]):
        return 1
    elif (BPDU1[0] == BPDU2[0] and BPDU1[1] == BPDU2[1] and BPDU1[2] == BPDU2[2] and BPDU1[3] < BPDU2[3]):
        return 1
    else:
        return 0


class bridge:
    def __init__(self, bridge_ID, port_list):
        self.bridge_ID = bridge_ID
        self.port_list = port_list  # port_list[0] is the port with port number 0
        self.config_BPDU = [bridge_ID, 0, bridge_ID,
                            None]  # Root ID, Cost, Transmitting Bridge ID, Transmitting Mac Address
        self.receive_queue = {}

    def initialize_recv_queue(self, bridges_dict):
        for b in bridges_dict:
            self.receive_queue[b] = []

    def set_bridge(self, bridge_ID, num_ports, mac_addresses):
        self.bridge_ID = bridge_ID
        self.num_ports = num_ports
        self.port_list = port_list

    def get_port(self, bridge_number, bridges_dict):
        for i in range(len(self.port_list)):
            if (bridge_number in self.port_list[i].get_reachable_bridge_ID(bridges_dict, self.bridge_ID)):
                return i

    def find_best_BPDUs_received(self, bridges_dict):
        # Select best BPDU at each bridge
        best_BPDUs_recvd = {}  # Bridge Number : BPDU
        # Write your code here
        return best_BPDUs_recvd

    def update_ports(self, bridges_dict, best_BPDUs_recvd):
        # Write your code here
        pass

    def elect_root(self, bridges_dict, best_BPDUs_recvd):
        # Write your code here
        pass

    def send_BPDUs(self, bridges_dict):
        # Write your code here
        return (bridges_dict)

    def receive_BPDUs(self, bridges_dict):
        # These functions are here to give you some structure
        # Feel free to ignore them and implement your own
        # Find best BPDU received from each bridge
        best_BPDUs_recvd = self.find_best_BPDUs_received(bridges_dict)

        # Compare BPDUs with those received at non-root ports
        self.update_ports(bridges_dict, best_BPDUs_recvd)

        # Find root bridge
        self.elect_root(bridges_dict, best_BPDUs_recvd)

        # Update dictionary and return
        bridges_dict[self.bridge_ID] = self
        return bridges_dict

    def get_root_port_id(self):
        for p in range(len(self.port_list)):
            if self.port_list[p].port_type == 2:
                return p
        return None

    def get_config_BPDU_at_port(self, port_number):
        BPDU_at_port = self.config_BPDU
        BPDU_at_port[3] = self.port_list[port_number].mac_address
        return (BPDU_at_port)

    def print_bridge(self):
        print("~~~~~~Bridge ID: " + str(self.bridge_ID) + " Root ID: " + str(self.config_BPDU[0]) + "~~~~~~")
        print("BPDU:")
        print(self.config_BPDU)

        print("MAC address | Port Type | Segment Number")
        for port in self.port_list:
            port.print_port()
