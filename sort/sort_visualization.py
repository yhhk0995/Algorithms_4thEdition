# import yhhk_sort as sort
import matplotlib.pyplot as plt
import numpy as np
import copy
import time


def main():
    np.random.seed(time.localtime())
    array = np.random.randint(1000, size=20)
    fig = plt.figure()
    plt.ion()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    length = len(array)
    x = range(length)

    ax.bar(x, array, align='center', color='yellow')
    plt.pause(0.2)

    for i in range(length):
        issorted = True
        for j in range(0, length-i-1, 1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
                ax.clear()
                ax.bar(x, array, align='center', color='yellow')
                matrix = [0]*length
                matrix[j+1] = array[j+1]
                for k in range(length-i, length, 1):
                    matrix[k] = array[k];
                ax.bar(x, matrix, align='center', color='red')
                issorted = False
            matrix = [0]*length
            matrix[j] = array[j]
            ax.bar(x, matrix, align='center', color='gray')
            plt.pause(0.2)
        if issorted:
            break

    plt.ioff()
    plt.show()

    # print(array)


if __name__ == '__main__':
    main()
