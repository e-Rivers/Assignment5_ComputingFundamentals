def mergeSort(arr, start, end):
    if(start < end):
        half = (start + end) // 2
        mergeSort(arr, start, half)
        mergeSort(arr, half + 1, end)
        return merge(arr, start, half, end)

def merge(arr, start, half, end):
    leftHalf = arr[start:half + 1]
    rightHalf = arr[half + 1:end + 1]

    i = j = 0
    k = start

    while(i < len(leftHalf) and j < len(rightHalf)):
        if(leftHalf[i] < rightHalf[j]):
            arr[k] = leftHalf[i]
            i += 1
        else:
            arr[k] = rightHalf[j]
            j += 1
        k += 1

    while(i < len(leftHalf)):
        arr[k] = leftHalf[i]
        i += 1
        k += 1

    while(j < len(rightHalf)):
        arr[k] = rightHalf[j]
        j += 1
        k += 1
        
    return arr
