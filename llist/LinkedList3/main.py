# from node import Node


"""
LinkedList articles: https://realpython.com/linked-lists-python/
 https://www.codingninjas.com/blog/2021/09/14/linked-lists-in-python/


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList()
print(llist)
first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")

first_node.next = second_node
second_node.next = third_node

print(llist)
