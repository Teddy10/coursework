import numpy as np
import timeit
import tree
from matplotlib import pyplot as plt


def sin_function(dee_jay2, diff, s):
    new_angle = dee_jay2 - diff
    result = s*np.sin(new_angle)
    return result
# dee_jay2 = d[j][2]


def cos_function(dee_jay2, diff, s):
    new_angle = dee_jay2 - diff
    result = s*np.cos(new_angle)
    return result


def add_function(dee_jay_i, vector_displacement):
    result = dee_jay_i + vector_displacement
    return result
# dee_jay_i = d[j][i], with i = 0,1,2


def merging_function(left_array, right_array):
    result = np.hstack((left_array, right_array))
    return result


def np_process(plot, local_multiplier, local_offset, local_scaling, local_iterations):
    parent_zero = np.array([0])    # aka d[j][0]
    parent_one = np.array([1])     # aka d[j][1]
    parent_two = np.array([0])     # aka d[j][2]

    if plot:
        plt.figure()
        plt.plot([0, 0], [0, 1])

    for i in range(local_iterations):

        left_temp_child_zero = sin_function(parent_two, local_offset, local_multiplier)
        left_child_zero = parent_zero + left_temp_child_zero

        left_temp_child_one = cos_function(parent_two, local_offset, local_multiplier)
        left_child_one = parent_one + left_temp_child_one

        left_child_two = parent_two - local_offset

        right_temp_child_zero = sin_function(parent_two, -local_offset, local_multiplier)
        right_child_zero = parent_zero + right_temp_child_zero

        right_temp_child_one = cos_function(parent_two, -local_offset, local_multiplier)
        right_child_one = parent_one + right_temp_child_one

        right_child_two = parent_two + local_offset

        if plot:
            plt.plot([parent_zero, left_child_zero], [parent_one, left_child_one])
            plt.plot([parent_zero, right_child_zero], [parent_one, right_child_one])

        local_multiplier *= local_scaling
        parent_zero = merging_function(left_child_zero, right_child_zero)
        parent_one = merging_function(left_child_one, right_child_one)
        parent_two = merging_function(left_child_two, right_child_two)
    if plot:
        plt.savefig('np_tree.png')

# # The command below can be used to check if the above code works. It creates the tree in another image
# # called "np_tree.png"
# np_process(True, 1, 0.1, 0.6, 5)


# The code below inserts the time complexity graph, in the case where numpy array operations are used, in a
# new image called "np_perf_plot.png"
final_iteration = 12
step = 1

iterations = list(range(1, final_iteration, step))
time_with_np = list(range(1, final_iteration, step))
time_without_np = list(range(1, final_iteration, step))

for i in iterations:
    time_with_np[iterations.index(i)] = timeit.timeit(lambda: np_process(False, 1, 0.1, 0.6, i), number=1000)
    time_without_np[iterations.index(i)] = timeit.timeit(lambda: tree.process(False, 1, 0.1, 0.6, i), number=1000)
# puts the time needed by the code for i tree levels in the time(i) (not time[i]!) element


plt.figure()
plt.xlabel("Number of iterations")
plt.ylabel("Time needed to create the tree(s)")
plt.title("Time complexity comparison")
plt.plot(iterations, time_with_np)
plt.plot(iterations, time_without_np)
plt.savefig('np_perf_plot.png')
