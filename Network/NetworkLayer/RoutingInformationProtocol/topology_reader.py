from Network.NetworkLayer.RoutingInformationProtocol.port import port_link, port
from Network.NetworkLayer.RoutingInformationProtocol.router import router


def topology_to_routers(topology):
    router_list = []
    for rtr in topology:
        r = router(rtr[0], [], [])
        for prt in rtr[1:]:
            new_link = port_link(prt[1], prt[2], prt[3])
            new_port = port(prt[0], new_link)
            r.add_port(new_port)
        r.add_RIP_entry(None, rtr[0], 0, None)
        router_list.append(r)
    return (router_list)
