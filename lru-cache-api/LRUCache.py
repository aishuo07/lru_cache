class LruCache:
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        arrange_nodes(self.head, self.tail)
        self.capacity = capacity
        self.keyNodeMap = {}

    def get(self, key):
        if key in self.keyNodeMap:
            res_node = self.keyNodeMap[key]
            ans = res_node.val
            self.delete_node(res_node)
            self.addNode(res_node)
            self.keyNodeMap[key] = self.head.next
            return ans
        return -1

    def put(self, key, value) -> None:
        if key in self.keyNodeMap:
            curr = self.keyNodeMap[key]
            self.delete_node(curr)

        if len(self.keyNodeMap) == self.capacity:
            self.delete_node(self.tail.prev)

        self.addNode(Node(key, value))
        self.keyNodeMap[key] = self.head.next

    def setCapacity(self, new_capacity: int):
        self.capacity = new_capacity

    def addNode(self, new_node):
        temp = self.head.next
        arrange_nodes(self.head, new_node)
        arrange_nodes(new_node, temp)

    def delete_node(self, del_node):
        del self.keyNodeMap[del_node.key]
        previous_to_del = del_node.prev
        next_to_del = del_node.next
        arrange_nodes(previous_to_del, next_to_del)



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


def arrange_nodes(prev_node: Node, next_node: Node):
    prev_node.next = next_node
    next_node.prev = prev_node


