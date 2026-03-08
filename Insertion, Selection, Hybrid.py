def insertionSort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j+1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break

        arr[j+1] = key

    return arr, comparisons, swaps

def selectionSort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps

def hybridSort(theSeq, threshold=10):

    if len(theSeq) <= threshold:
        sorted_arr, comp, swap = insertionSort(theSeq)
    else:
        sorted_arr, comp, swap = selectionSort(theSeq)

    return sorted_arr, comp, swap