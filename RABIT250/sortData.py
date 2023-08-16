import re
import numpy as np

import argparse

parser = argparse.ArgumentParser(description="Read a file")
parser.add_argument("--file", type=str, help="File to read", default="output.txt")

args = parser.parse_args()
file_to_read = "results/" + args.file

# Initialize empty lists
sequential_times = []
parallel_times = []

lower_percentile = 5
higher_percentile = 95
la = 1

# Open and read the file
with open(file_to_read, 'r') as file:
    lines = file.readlines()

    # Regular expressions to match the lines with times
    sequential_re = re.compile(r'Time used\(ms\) for Original Version: (\d+) ms.')
    parallel_re = re.compile(r'Time used\(ms\) for Parallel Version: (\d+) ms.')

    # Loop through lines
    for line in lines:
        # If the line matches the regular expression for sequential time, add the time to the list
        match_sequential = sequential_re.search(line)
        if match_sequential:
            sequential_times.append(int(match_sequential.group(1)))

        # If the line matches the regular expression for parallel time, add the time to the list
        match_parallel = parallel_re.search(line)
        if match_parallel:
            parallel_times.append(int(match_parallel.group(1)))

def filter_to_confidence_interval(numbers, lower_percentile, higher_percentile):
    # calculate 5th and 95th percentile to create 90% confidence interval
    lower_bound = np.percentile(numbers, lower_percentile)
    upper_bound = np.percentile(numbers, higher_percentile)

    # filter list to only numbers within the confidence interval
    filtered_numbers = [num for num in numbers if lower_bound <= num <= upper_bound]
    outside_interval = [num for num in numbers if num not in filtered_numbers]

    return filtered_numbers, outside_interval

# # print the average times:
# time1 = sum(sequential_times)/len(sequential_times)
# time2 = sum(parallel_times)/len(parallel_times)
# print("Sequential times:", time1)
# print("Parallel times:", time2)
#

filtered_sequential_times, outside_sequential_times = filter_to_confidence_interval(sequential_times, lower_percentile, higher_percentile)
filtered_parallel_times, outside_parallel_times = filter_to_confidence_interval(parallel_times, lower_percentile, higher_percentile)
# print the average times:
time1 = sum(sequential_times)/len(sequential_times)
time2 = sum(parallel_times)/len(parallel_times)
print("Sequential times:", time1)
print("Parallel times:", time2)
print("enhanced: ", (time1-time2)*100/time1, "%")
print()

# After filtered
time3 = sum(filtered_sequential_times)/len(sequential_times)
time4 = sum(filtered_parallel_times)/len(parallel_times)
print("90% of data for Sequential times:", time3)
print("90% of data for Parallel times:", time4)
print("enhanced: ", (time3-time4)*100/time3, "%")
print()

import matplotlib.pyplot as plt
# ============================================================================================================
# NOTICE: Draw all the points and 90% of these points

# def plot_points(plt, numbers, la, color):
#     # create a list with 'la' repeated as many times as there are elements in 'numbers'
#     x_values = [la] * len(numbers)
#
#     # create the scatter plot
#     plt.scatter(x_values, numbers, color=color)
#
#     # optionally set labels for x and y axis
#     plt.xlabel('la')
#     plt.ylabel('Times(ms)')
#
#
# all_sequential_times = [filtered_sequential_times, filtered_sequential_times, filtered_sequential_times]
# for filtered_sequential_times in all_sequential_times:
#     plot_points(plt, filtered_sequential_times, la, 'blue')
#     plot_points(plt, outside_sequential_times, la, 'red')
#     la = la + 1
#
# upper_bounds = [max(filtered_sequential_times) for filtered_sequential_times in all_sequential_times]
# plt.plot([1,2,3], upper_bounds, color='red', label='Upper bound')
#
# lower_bounds = [min(filtered_sequential_times) for filtered_sequential_times in all_sequential_times]
# plt.plot([1,2,3], lower_bounds, color='orange', label='Lower bound')
#
# # plot_points(plt, filtered_parallel_times, la, 'orange')
# # plot_points(plt, outside_parallel_times, la, 'green')
#
# # display the plot
#
# # plt.show()
#
# plt.legend()
# # plt.show()

# ============================================================================================================
# NOTICE: Draw the spots and the curve

# y_coords = [16, 28, 32, 45, 59, 45, 34, 32, 21, 12]
# x_coords = [1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 2.9, 3.1]
#
# # 使用numpy的函数对点进行插值以获得曲线
# curve = np.poly1d(np.polyfit(x_coords, y_coords, 3))
#
# # 定义用于绘制曲线的x值
# x_curve = np.linspace(min(x_coords), max(x_coords), 1000)
# y_curve = curve(x_curve)
#
# # 绘制点
# plt.scatter(x_coords, y_coords, c='red')
# # 绘制曲线
# plt.plot(x_curve, y_curve, c='blue')
#
# plt.title('The influence of density')
# plt.xlabel('density(td)')
# plt.ylabel('time(ms)')
#
# plt.show()
# ============================================================================================================
# plot the graph of points, where each two points are linked by a line

# Data points
# x = list(range(6))
# y1 = [42.52, 51.34, 65.46, 69.95, 55.43, 48.97]
# y2 = [40.52, 55.34, 62.46, 67.95, 50.43, 42.97]
#
# # Plotting the first set of data points
# plt.scatter(x, y1, color='blue', marker='o', label=None)
# plt.plot(x, y1, color='red', label='td=1.3')
#
# # Plotting the second set of data points
# plt.scatter(x, y2, color='green', marker='x', label=None)
# plt.plot(x, y2, color='purple', label='td=1.3 (2nd set)')
#
# # Labelling the x and y axes
# plt.xlabel("Index")
# plt.ylabel("Value")
#
# # Displaying the title
# plt.title("Graph of Given Points")
#
# # Displaying the legend
# plt.legend(loc='upper left')
#
# # Displaying the graph
# # plt.grid(True)
# plt.tight_layout()
# plt.show()

