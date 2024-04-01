def quickSort(arr, start, end):
    if(start < end):
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)
    return arr

def partition(a, start, end):
    pivot, elempivot = start, a[start]
    j = start
    for i in range(start + 1, end + 1):
        if(a[i] < elempivot):
            j += 1
            a[i], a[j] = a[j], a[i]
    pivot = j
    a[start], a[pivot] = a[pivot], a[start]
    return pivot
