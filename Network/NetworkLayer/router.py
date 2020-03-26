from rip_packet import RIP_entry
from rip_packet import RIP_packet
from port import port
from port import port_link


class router_base:
    def __init__(self, IP_address, rip_entries, ports):
        self.IP_address = IP_address
        self.rip_entries = rip_entries
        self.ports = ports

    def add_port(self, prt):
        self.ports.append(prt)

    def add_RIP_entry(self, port_IP, dest_IP, cost, next_hop_IP):
        new_rip_entry = RIP_entry(port_IP, cost, dest_IP, next_hop_IP)
        self.rip_entries.append(new_rip_entry)

    def find_RIP_entry(self, destination_IP_to_find):
        for entry in self.rip_entries:
            if (entry.dest_IP_address == destination_IP_to_find):
                return entry
        return None

    def set_RIP_entry_cost(self, destination_IP_to_find, new_cost):
        for i in self.rip_entries:
            if (entry.dest_IP_address == destination_IP_to_find):
                entry.set_cost(new_cost)
        return None

    def delete_RIP_entry(self, destination_IP_to_find):
        for entry in self.rip_entries:
            if (entry.dest_IP_address == destination_IP_to_find):
                self.rip_entries.remove(entry)

    def print_router(self):
        print("~~~~ Router IP address = " + str(self.IP_address) + "~~~~")
        print("---Ports---")
        print("Port IP | Destination Router IP | Destination Port IP | Cost")
        for p in self.ports:
            p.print_port()
        print("---RIP entries---")
        print("port IP | destination IP address | next hop | cost")
        for re in self.rip_entries:
            re.print_rip_entry()

    def return_router(self):
        r = []
        r.append("~~~~ Router IP address = " + str(self.IP_address) + "~~~~")
        r.append("---Ports---")
        r.append("Port IP | Destination Router IP | Destination Port IP | Cost")
        for p in self.ports:
            r.append(p.return_port())
        r.append("---RIP entries---")
        r.append("port IP | destination IP address | next hop | cost")
        for re in self.rip_entries:
            r.append(re.return_rip_entry())
        return r


class router(router_base):
    def send_RIP_packets(self, routers):
        # Write your code here
        return routers

    def receive_RIP_packets(self, rip_packet, link_send_on, routers, next_hop_IP):
        # Write your code here
        return routers
