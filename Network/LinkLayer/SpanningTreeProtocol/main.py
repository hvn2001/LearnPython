from Network.LinkLayer.SpanningTreeProtocol.simulator import simulator


def main():
    bridges = [
        [
            100,  # bridge_ID
            [  # list of ports
                [0, 0],  # each port is mac_address, segment_number
                [1, 1]
            ]
        ],
        [
            200,
            [
                [2, 1],
                [3, 2]
            ]
        ],
        [
            300,
            [
                [4, 2],
                [5, 3]
            ]
        ],
    ]

    # Scenario
    end_time = 800

    simulator(bridges, end_time)


main()
'''
before STP
~~~~~~Bridge ID: 200 Root ID: 200~~~~~~
BPDU:
[200, 0, 200, None]
MAC address | Port Type | Segment Number
2 |  Forwarding |  1
3 |  Forwarding |  2
~~~~~~Bridge ID: 300 Root ID: 300~~~~~~
BPDU:
[300, 0, 300, None]
MAC address | Port Type | Segment Number
4 |  Forwarding |  2
5 |  Forwarding |  3
~~~~~~Bridge ID: 100 Root ID: 100~~~~~~
BPDU:
[100, 0, 100, None]
MAC address | Port Type | Segment Number
0 |  Forwarding |  0
1 |  Forwarding |  1
after STP
~~~~~~Bridge ID: 200 Root ID: 100~~~~~~
BPDU:
[100, 1, 200, 3]
MAC address | Port Type | Segment Number
2 |  Root |  1
3 |  Forwarding |  2
~~~~~~Bridge ID: 300 Root ID: 100~~~~~~
BPDU:
[100, 2, 300, 4]
MAC address | Port Type | Segment Number
4 |  Root |  2
5 |  Forwarding |  3
~~~~~~Bridge ID: 100 Root ID: 100~~~~~~
BPDU:
[100, 0, 100, 1]
MAC address | Port Type | Segment Number
0 |  Forwarding |  0
1 |  Forwarding |  1
'''
