from __future__ import absolute_import, division, print_function

import numpy as np

def generateInstance(class_list=['a', 'b'], 
                     xmin=0.0, xmax=1.0, ymin=0.0, ymax=1.0):
    """Generate an instance of example line, in the format of 
    class_name, x_coordinate, y_coordinate.
    
    Args:
    class_list: a list of class names, each class name is a string.

    Returns:
    instance_line: a string in the format of "class_name, x, y"
    """
    instance_line = ", ".join([np.random.choice(class_list),
                               str(xmin + np.random.random() * (xmax - xmin)),
                               str(ymin + np.random.random() * (ymax - ymin))])
    return instance_line

def main():
    filename = "testdata.txt"
    N = 100
    with open(filename, "w") as f:
        for i in range(N):
          line = generateInstance()
          f.write(line + "\n")

if __name__ == "__main__":
    main()

    
    
