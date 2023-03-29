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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        pass

    def pop(self):
        # if linked list is empty
        if self.head is None:
            return None
        
        # O(N)
        prev = self.head
        cur = self.head

        while cur.next is not None:
            prev = cur
            cur = cur.next
        
        self.tail = prev
        self.tail.next = None
        self.lenght -= 1

        if self.lenght == 0:
            self.head = None
            self.tail = None
        return cur

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
    print("Value : ", my_linked_list.pop().value)
    print("Value : ", my_linked_list.pop().value)
    print("Value : ", my_linked_list.pop())
    my_linked_list.print_list()

