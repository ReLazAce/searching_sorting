def findFirst(arr, target):
    left = 0
    right = len(arr) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            first = mid          # simpan posisi
            right = mid - 1      # cari lebih kiri lagi
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first


def findLast(arr, target):
    left = 0
    right = len(arr) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last = mid          # simpan posisi
            left = mid + 1      # cari lebih kanan lagi
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last


def countOccurrences(sortedList, target):
    first = findFirst(sortedList, target)

    if first == -1:
        return 0

    last = findLast(sortedList, target)

    return last - first + 1