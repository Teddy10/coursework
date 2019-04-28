import timeit
from matplotlib import pyplot as plt
import tree

final_iteration = 12
step = 1

iterations = list(range(1, final_iteration, step))
time = list(range(1, final_iteration, step))

for i in iterations:
    time[iterations.index(i)] = timeit.timeit(lambda: tree.process(False, 1, 0.1, 0.6, i), number=1000)
# puts the time needed by the code for i tree levels in the time(i) (not time[i]!) element

plt.figure()
plt.xlabel("Number of iterations")
plt.ylabel("Time needed to create the tree(s)")
plt.title("Time complexity without the use of NumPy")

plt.plot(iterations, time)
plt.savefig('perf_plot.png')





