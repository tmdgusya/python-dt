class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # value is the value of first node
    def __init__(self, value):
        # create a node with value
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
        pass

    def append(self, value):
        # create a node with value
        new_node = Node(value)
        # add Node to the end of the list
        self.tail.next = new_node
        self.tail = new_node
        self.lenght += 1
        pass

    def prepend(self, value):
        # create a node with value

        # add Node to the beginning of the list
        pass

    def insert(self, index, value):
        # create a node with value

        # insert that node at the given index
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    my_linked_list.append(5)
    my_linked_list.print_list()
