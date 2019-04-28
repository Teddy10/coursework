from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


def f_refactoring_fun(arg, dj, diff, s):
    result = dj[arg] + s*sin(dj[2] - diff)
    return result


def s_refactoring_fun(arg, dj, diff, s):
    result = dj[arg] + s*cos(dj[2] - diff)
    return result


def process(plot, local_multiplier, local_offset, local_scaling, local_iterations):

    parent = [[0, 1, 0]]
    horizontal_axis = [0, 0]
    vertical_axis = [0, 1]

    if plot:
        plt.plot(horizontal_axis, vertical_axis)

    for i in range(local_iterations):
        child = []
        for dee_jay in parent:
            f_app_x = f_refactoring_fun(0, dee_jay, local_offset, local_multiplier)
            f_app_y = s_refactoring_fun(1, dee_jay, local_offset, local_multiplier)
            f_app_z = dee_jay[2] - local_offset
            first_addition = [f_app_x, f_app_y, f_app_z]
            child.append(first_addition)

            s_app_x = f_refactoring_fun(0, dee_jay, -local_offset, local_multiplier)
            s_app_y = s_refactoring_fun(1, dee_jay, -local_offset, local_multiplier)
            s_app_z = dee_jay[2] + local_offset
            second_addition = [s_app_x, s_app_y, s_app_z]
            child.append(second_addition)

            if plot:
                # plt.plot(horizontal_axis, vertical_axis)
                first_pl_x = [dee_jay[0], child[-2][0]]
                first_pl_y = [dee_jay[1], child[-2][1]]
                plt.plot(first_pl_x, first_pl_y)

                second_pl_x = [dee_jay[0], child[-1][0]]
                second_pl_y = [dee_jay[1], child[-1][1]]
                plt.plot(second_pl_x, second_pl_y)

        parent = child
        local_multiplier *= local_scaling
    if plot:
        plt.savefig('tree.png')


if __name__ == "__main__":
    parser = ArgumentParser(description="Trees")

    parser.add_argument('multiplier')
    parser.add_argument('offset')
    parser.add_argument('scaling')
    parser.add_argument('number_of_iterations')

    arguments = parser.parse_args()

    multiplier = int(arguments.multiplier)
    offset = float(arguments.offset)
    scaling = float(arguments.scaling)
    number_of_iterations = int(arguments.number_of_iterations)
    process(True, multiplier, offset, scaling, number_of_iterations)

