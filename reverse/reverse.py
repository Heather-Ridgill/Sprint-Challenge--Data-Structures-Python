class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

# A -> B -> C -> D -> 0 (INITIAL)
# D -> C -> B -> A -> 0 (REVERSAL)
# A <- B <- C <- D <- 0 (MOVES OPPOSITE)


    def reverse_list(self, node, prev):
        if node is None:
            return 
        # if next node is none 
        if node.next_node is None:
        # new head becomes current node
            self.head = node
            #next node of the new head = value of prev
            node.next_node = prev
        # not at the end
        else:
            # saving next in temporary variable
            next_node = node.next_node
            # reversing.. point current node to previous node
            # prev node becomes current
            node.next_node = prev
            self.reverse_list(next_node, node)





