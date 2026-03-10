def mergeThreeSortedLists(listA, listB, listC):

    i = j = k = 0
    result = []

    while i < len(listA) or j < len(listB) or k < len(listC):

        a = listA[i] if i < len(listA) else float('inf')
        b = listB[j] if j < len(listB) else float('inf')
        c = listC[k] if k < len(listC) else float('inf')

        smallest = min(a, b, c)

        result.append(smallest)

        if smallest == a:
            i += 1
        elif smallest == b:
            j += 1
        else:
            k += 1

    return result