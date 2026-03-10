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

arr = [3,1,2]

print("Naive:", countInversionsNaive(arr.copy()))
print("Smart:", countInversionsSmart(arr.copy()))