import pytest
import random

from tree_builder import new_treemap, treemap_insert, treemap_search, \
    treemap_search_between


# This creates a "test fixture". This is an easy way to create data that's
# needed by your tests, and if one test changes the data in some way, the
# other tests get a clean untouched copy.
@pytest.fixture
def example_tree():
    example = new_treemap(4, "ducks")
    treemap_insert(example, 3, "walruses")
    treemap_insert(example, 3.5, "penguins")
    treemap_insert(example, 2, "seals")
    treemap_insert(example, 5, "whales")
    treemap_insert(example, 4.5, "otters")

    # More examples
    example2 = new_treemap(0, "apple")
    treemap_insert(example2, -1, "pear")
    treemap_insert(example2, -1, "pineapple")
    treemap_insert(example2, -1, "watermellon")
    treemap_insert(example2, 9, "orange")
    treemap_insert(example2, -3.4, "berry")
    treemap_insert(example2, 5, "mango")

    # Random tree
    info = {
        0: "apple",
        -1: "watermellon",
        9: "orange",
        -3.4: "berry",
        5: "mango"}
    keys = list(info.keys())
    values = list(info.values())
    order = [0, 1, 2, 3, 4]
    random.shuffle(order)
    example3 = new_treemap(keys[order[0]], values[order[0]])
    treemap_insert(example3, keys[order[1]], values[order[1]])
    treemap_insert(example3, keys[order[2]], values[order[2]])
    treemap_insert(example3, keys[order[3]], values[order[3]])
    treemap_insert(example3, keys[order[4]], values[order[4]])

    return [example, example2, example3]


def test_treemap_search(example_tree):
    assert treemap_search(example_tree[0], 4) == "ducks"
    assert treemap_search(example_tree[0], 2) == "seals"
    assert treemap_search(example_tree[1], -1) == "watermellon"
    assert treemap_search(example_tree[1], -3.4) == "berry"
    assert treemap_search(example_tree[2], -1) == "watermellon"
    assert treemap_search(example_tree[2], -3.4) == "berry"

    with pytest.raises(KeyError):
        treemap_search(example_tree[0], 17)
    with pytest.raises(KeyError):
        treemap_search(example_tree[1], 1)
    with pytest.raises(KeyError):
        treemap_search(example_tree[2], 1)


def test_treemap_search_between(example_tree):
    assert treemap_search_between(example_tree[0], 2, 3) == ["seals"]
    assert treemap_search_between(example_tree[0], 2, 3.5) == \
        ["seals", "walruses"]
    assert treemap_search_between(example_tree[1], -3.4, 5) == \
        ['berry', 'watermellon', 'apple']
    assert treemap_search_between(example_tree[2], -3.4, 5) == \
        ['berry', 'watermellon', 'apple']
