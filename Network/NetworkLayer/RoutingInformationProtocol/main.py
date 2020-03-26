from Network.NetworkLayer.RoutingInformationProtocol.topology_reader import topology_to_routers


def main():
    topology2 = [
        [1, [11, 2, 21, 1], [12, 4, 41, 1]],  # Routers and links
        [2, [21, 1, 11, 1], [22, 5, 53, 1], [23, 3, 31, 1]],
        # [IP of router, [link of router, IP of destination router, IP of link of destination router, cost]]
        [3, [31, 2, 23, 1], [32, 5, 52, 1]],
        [4, [41, 1, 12, 1], [42, 5, 51, 1]],
        [5, [51, 4, 42, 1], [52, 3, 32, 1], [53, 2, 22, 1]]
    ]
    topology = [
        [1, [11, 2, 21, 1], [12, 4, 41, 5]],  # Routers and links
        [2, [21, 1, 11, 1], [22, 5, 53, 1], [23, 3, 31, 4]],
        # [IP of router, [link of router, IP of destination router, IP of link of destination router, cost]]
        [3, [31, 2, 23, 4], [32, 5, 52, 1]],
        [4, [41, 1, 12, 5], [42, 5, 51, 1]],
        [5, [51, 4, 42, 1], [52, 3, 32, 1], [53, 2, 22, 1]]
    ]
    steps_to_run = 5
    router_list = topology_to_routers(topology)
    print("---------routers initialized---------")
    for r in router_list:
        r.print_router()

    # Simulator
    for i in range(steps_to_run):
        for j in range(len(router_list)):
            router_list = router_list[j].send_RIP_packets(router_list)
    print("---------routers after " + str(i) + " iterations---------")
    for r in router_list:
        r.print_router()


main()
'''
---------routers initialized---------
~~~~ Router IP address = 1~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
11 | 2 | 21 | 1
12 | 4 | 41 | 5
---RIP entries---
port IP | destination IP address | next hop | cost
None | 1 | None | 0
~~~~ Router IP address = 2~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
21 | 1 | 11 | 1
22 | 5 | 53 | 1
23 | 3 | 31 | 4
---RIP entries---
port IP | destination IP address | next hop | cost
None | 2 | None | 0
~~~~ Router IP address = 3~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
31 | 2 | 23 | 4
32 | 5 | 52 | 1
---RIP entries---
port IP | destination IP address | next hop | cost
None | 3 | None | 0
~~~~ Router IP address = 4~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
41 | 1 | 12 | 5
42 | 5 | 51 | 1
---RIP entries---
port IP | destination IP address | next hop | cost
None | 4 | None | 0
~~~~ Router IP address = 5~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
51 | 4 | 42 | 1
52 | 3 | 32 | 1
53 | 2 | 22 | 1
---RIP entries---
port IP | destination IP address | next hop | cost
None | 5 | None | 0
---------routers after 4 iterations---------
~~~~ Router IP address = 1~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
11 | 2 | 21 | 1
12 | 4 | 41 | 5
---RIP entries---
port IP | destination IP address | next hop | cost
None | 1 | None | 0
11 | 2 | 2 | 1
12 | 4 | 2 | 3
11 | 3 | 2 | 3
11 | 5 | 2 | 2
~~~~ Router IP address = 2~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
21 | 1 | 11 | 1
22 | 5 | 53 | 1
23 | 3 | 31 | 4
---RIP entries---
port IP | destination IP address | next hop | cost
None | 2 | None | 0
21 | 1 | 1 | 1
23 | 3 | 5 | 2
22 | 5 | 5 | 1
22 | 4 | 5 | 2
~~~~ Router IP address = 3~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
31 | 2 | 23 | 4
32 | 5 | 52 | 1
---RIP entries---
port IP | destination IP address | next hop | cost
None | 3 | None | 0
31 | 2 | 5 | 2
31 | 1 | 5 | 3
32 | 5 | 5 | 1
32 | 4 | 5 | 2
~~~~ Router IP address = 4~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
41 | 1 | 12 | 5
42 | 5 | 51 | 1
---RIP entries---
port IP | destination IP address | next hop | cost
None | 4 | None | 0
41 | 1 | 5 | 3
42 | 5 | 5 | 1
42 | 2 | 5 | 2
42 | 3 | 5 | 2
~~~~ Router IP address = 5~~~~
---Ports---
Port IP | Destination Router IP | Destination Port IP | Cost
51 | 4 | 42 | 1
52 | 3 | 32 | 1
53 | 2 | 22 | 1
---RIP entries---
port IP | destination IP address | next hop | cost
None | 5 | None | 0
53 | 2 | 2 | 1
53 | 1 | 2 | 2
52 | 3 | 3 | 1
51 | 4 | 4 | 1
'''
