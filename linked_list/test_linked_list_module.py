# Implememt unit test for class Node and LinkedList


from linked_list_module import Node, LinkedList

# Instantiate an empty node
node = Node()

# Test methods in Node


def test_set_data():
    # Set data for node
    node.set_data(10)
    assert node.data == 10
    node.set_data("test")
    assert node.data == "test"

# Instantiate an empty list


linked_list = LinkedList()

# Insert numbers into the list
linked_list.insert(11)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

# Test methods in LinkedList


def test_str():
    """This is to test the str() method"""

    assert str(linked_list) == "11 3 6 3 11 6 5 7 5 "


def test_insert():
    """This is to test the insert method"""

    linked_list.insert(8)
    assert str(linked_list) == "11 3 6 3 11 6 5 7 5 8 "
    linked_list.insert(18)
    assert str(linked_list) == "11 3 6 3 11 6 5 7 5 8 18 "
    linked_list.insert(1)
    assert str(linked_list) == "11 3 6 3 11 6 5 7 5 8 18 1 "


def test_remove_deplicate():
    """This is to test the remove_duplicate method"""

    removed_list = linked_list.remove_duplicates()
    assert str(removed_list) == "11 3 6 5 7 8 18 1 "


def test_size():
    """This is to test the size method"""

    assert linked_list.size() == 12
    linked_list.insert(8)
    assert linked_list.size() == 13
