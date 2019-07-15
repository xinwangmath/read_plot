from __future__ import absolute_import, division, print_function

import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict

def readFromFile(filename):
    """
    Read data from file and save in a dict with key = class_name, 
    value = [[x_1, y_1], [x_2, y_2], ...]. 

    Args:
    filename: string of input file name;

    Returns:
    data_dict: dict, key = class_name, value = [[x_1, y_1], [x_2, y_2], ...].

    Assuming file is in the format of 
    class_name_1, x, y
    class_name_2, x, y
    ...
    """
    data_dict = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            class_name, x_str, y_str = line.split(",")
            data_dict[class_name].append([float(x_str), float(y_str)])
    return data_dict

def main():
    filename = "testdata.txt"
    data_dict = readFromFile(filename)
    print(data_dict)
    count = 1
    for class_name in data_dict:
        xy_matrix = np.array(data_dict[class_name])
        xy_matrix = np.sort(xy_matrix, axis=0)  # sort (x, y) pairs by the x coordinates

        plt.subplot(len(data_dict), 1, count)
        plt.plot(xy_matrix[:, 0], xy_matrix[:, 1])
        plt.title("class name = {}".format(class_name))
        plt.xlabel("x")
        plt.ylabel("y")

        count += 1
    plt.tight_layout()  # adjust layout for sub-figures.
    plt.show()
    plt.savefig("test_plot.pdf")

if __name__ == "__main__":
    main()


            

