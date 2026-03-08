def bubbleSort(arr):
    arr = arr.copy()
    n = len(arr)

    total_comparisons = 0
    total_swaps = 0
    passes_used = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            total_comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                total_swaps += 1
                swapped = True

        passes_used += 1

        print(f"Pass {passes_used}: {arr}")

        # Early termination
        if not swapped:
            break

    return (arr, total_comparisons, total_swaps, passes_used)