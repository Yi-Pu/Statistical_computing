from random_walker_module import RandomWalker, ModifiedRandomWalker
import matplotlib.pyplot as plt

# The solution for problem (b)

# Instantiate 4 random walkers
rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
rw3 = RandomWalker()

# Create lists to save the trajectories
traj0 = [[], []]
traj1 = [[], []]
traj2 = [[], []]
traj3 = [[], []]

for i in range(1000):
    # Create a loop to make 1000 steps

    # Make a step
    rw0.step()
    # Save the current position
    traj0[0].append(rw0.get_x_pos())
    traj0[1].append(rw0.get_y_pos())

    # Make a step
    rw1.step()
    # Save the current position
    traj1[0].append(rw1.get_x_pos())
    traj1[1].append(rw1.get_y_pos())

    # Make a step
    rw2.step()
    # Save the current position
    traj2[0].append(rw2.get_x_pos())
    traj2[1].append(rw2.get_y_pos())

    # Make a step
    rw3.step()
    # Save the current position
    traj3[0].append(rw3.get_x_pos())
    traj3[1].append(rw3.get_y_pos())

# Plot all trajectories
plt.plot(traj0[0], traj0[1], color='g')
plt.plot(traj1[0], traj1[1], color='y')
plt.plot(traj2[0], traj2[1], color='b')
plt.plot(traj3[0], traj3[1], color='r')
plt.show()

# The solution to problem (d)

# Instantiate 3 random walkers and a modified random walker
rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
rw3 = ModifiedRandomWalker()

# Create lists to save the trajectories
traj0 = [[], []]
traj1 = [[], []]
traj2 = [[], []]
traj3 = [[], []]

for i in range(1000):
    # Create a loop to make 1000 steps

    # Make a step
    rw0.step()
    # Save the current position
    traj0[0].append(rw0.get_x_pos())
    traj0[1].append(rw0.get_y_pos())

    # Make a step
    rw1.step()
    # Save the current position
    traj1[0].append(rw1.get_x_pos())
    traj1[1].append(rw1.get_y_pos())

    # Make a step
    rw2.step()
    # Save the current position
    traj2[0].append(rw2.get_x_pos())
    traj2[1].append(rw2.get_y_pos())

    # Make a step
    rw3.step(r0=rw0, r1=rw1, r2=rw2)
    # Save the current position
    traj3[0].append(rw3.get_x_pos())
    traj3[1].append(rw3.get_y_pos())

# Plot all trajectories
plt.plot(traj0[0], traj0[1], color='g')
plt.plot(traj1[0], traj1[1], color='y')
plt.plot(traj2[0], traj2[1], color='b')
plt.plot(traj3[0], traj3[1], color='r')
plt.show()
