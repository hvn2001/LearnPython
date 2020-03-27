class Node:
    def __init__(self, name):
        self.node_name = name
        self.children = []


def create_xml_tree(xml):
    root = Node("Hello")
    return root
