def countInversionsNaive(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
                
    return count

def merge_and_count(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += (mid - i + 1)
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]

    return inv_count


def merge_sort_and_count(arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, left, mid)
        inv_count += merge_sort_and_count(arr, mid + 1, right)
        inv_count += merge_and_count(arr, left, mid, right)

    return inv_count


def countInversionsSmart(arr):
    return merge_sort_and_count(arr, 0, len(arr) - 1)

import random
import time

sizes = [1000, 5000, 10000]

for size in sizes:
    arr = [random.randint(0,10000) for _ in range(size)]

    start = time.time()
    countInversionsNaive(arr.copy())
    naive_time = time.time() - start

    start = time.time()
    countInversionsSmart(arr.copy())
    smart_time = time.time() - start

    print("Ukuran:", size)
    print("Naive Time:", naive_time)
    print("Smart Time:", smart_time)
    print()