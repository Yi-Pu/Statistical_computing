# This is to test the methods in random_walker_module

from random_walker_module import RandomWalker, ModifiedRandomWalker

# Instantiate 3 RandomWalkers and 1 ModifiedRandomWalker
rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
mrw = ModifiedRandomWalker()


def test_rw_step():
    # This is to test the step method in RandomWalker class
    rw0.step()
    rw1.step()
    rw2.step()

    assert rw0.x_pos != 0
    assert rw0.y_pos != 0

    assert rw1.x_pos != 0
    assert rw1.y_pos != 0

    assert rw2.x_pos != 0
    assert rw2.y_pos != 0


def test_mrw_step():
    # This is to test the step method in ModifiedRandomWalker class
    mrw.step(rw0, rw1, rw2)
    assert mrw.x_pos != 0
    assert mrw.y_pos != 0


def test_rw_getter():
    # This is to test the getter method in RandomWalker class
    rw0.get_x_pos == rw0.x_pos
    rw0.get_y_pos == rw0.y_pos

    rw1.get_x_pos == rw0.x_pos
    rw1.get_y_pos == rw0.y_pos

    rw2.get_x_pos == rw0.x_pos
    rw2.get_y_pos == rw0.y_pos


def test_mrw_getter():
    # This is to test the getter method in ModifiedRandomWalker class
    mrw.get_x_pos == mrw.x_pos
    mrw.get_y_pos == mrw.y_pos
