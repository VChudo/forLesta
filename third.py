from random import randint
from time import time


# Method to do Counting Sort
def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for _ in range(0, len(arr)):
        count_arr[arr[_] - min_element] += 1
    for _ in range(1, len(count_arr)):
        count_arr[_] += count_arr[_ - 1]
    for _ in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[_] - min_element] - 1] = arr[_]
        count_arr[arr[_] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    return arr


ar = [randint(0, 99) for _ in range(9999999)]
start = time()
count_sort(ar)
stop = time()
print(stop - start)
