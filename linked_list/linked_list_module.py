class Node:
    """Class for representing a node in a linked list"""

    def __init__(self):
        """This function is to initiate the attributes"""
        self.next = None
        self.data = None

    def set_data(self, data):
        """This funtion is the set data for a node"""
        self.data = data


class LinkedList:
    """Class to create and operate on a linked list"""

    def __init__(self):
        """This function is to initiate the attributes"""
        self.head = None

    def __str__(self):
        """Method for casting the linked list as a string

        Called by str() or print().

        Returns a string representation of the list.
        """

        if self.head is None:
            raise ValueError("List is empty")

        ret_str = ""
        current = self.head
        while current:
            ret_str = ret_str + str(current.data) + " "
            current = current.next
        return ret_str

    def insert(self, data):
        """Insert a node at the end of the linked list

        Parameters:

        data: data to be stored in the node
        """

        node = Node()
        node.set_data(data)
        current = self.head
        if current is None:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    def size(self):
        """Returns size of the linked list"""

        current = self.head
        if current is None:
            size = 0
        else:
            size = 0
            while (current):
                size = size + 1
                current = current.next
        return size

    def remove_duplicates(self):
        """Removes duplicate nodes from the linked list"""

        removed_list = LinkedList()
        current = self.head
        if current is None:
            raise ValueError("List is empty")
        else:
            if current.next is None:
                removed_list.insert(current.data)
            else:
                current_set = set()
                while (current):
                    if current.data in current_set:
                        pass
                    else:
                        removed_list.insert(current.data)
                    current_set.add(current.data)
                    current = current.next
        return removed_list
