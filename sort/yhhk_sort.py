# -*- coding: utf8 -*-
import copy


def main():
    array = [54, 454, 543, 67, 2, 34, 782, 4, 5, 46, 72, 123, 5473, 2435, 4532, 45, 45, 6, 6, 6, 7, 4326, 32, 6, 31, 7465, 345]
    arr = copy.deepcopy(array)
    bubble_sort(arr)
    print('bubble sort:')
    print(arr)
    arr = copy.deepcopy(array)
    select_sort(arr)
    print('select sort:')
    print(arr)
    arr = copy.deepcopy(array)
    insert_sort(arr)
    print('insert sort:')
    print(arr)
    arr = copy.deepcopy(array)
    insert_sort_enhance(arr)
    print('insert sort enhance:')
    print(arr)
    # TODO: 排序算法可视化


def bubble_sort(array):
    is_sorted = True
    for i in range(0, len(array), 1):
        for j in range(1, len(array)-i, 1):
            if array[j] < array[j-1]:
                (array[j], array[j-1]) = (array[j-1], array[j])  # 注意：python中没有必要swap两个变量的值，此处直接交换两个变量的标记。
                is_sorted = False
        if is_sorted:
            break


def select_sort(array):
    is_sorted = True
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array), 1):
            if array[j] < array[idx_min] :
                idx_min = j
                is_sorted = False
        if is_sorted:
            break
        (array[i], array[idx_min]) = (array[idx_min], array[i])


def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                (array[j],array[j-1]) = (array[j-1],array[j])


def insert_sort_enhance(array):  # 找到要插入的位置，将数组右侧部分整体右移，而不是一个一个地交换位置
    for i in range(1, len(array)):
        index = i
        for j in range(i, 0, -1):
            if array[i] < array[j-1]:
                index = j-1
        tmp = array[i]
        for j in range(i, index, -1):
            array[j] = array[j-1]
        array[index] = tmp


if __name__ == '__main__':
    main()
