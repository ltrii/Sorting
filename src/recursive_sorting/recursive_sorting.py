# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    s = 0
    for i in range(elements):
        if i >= len(arrA):
            merged_arr[i] = arrB[s]
            s += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        leftHalf = merge_sort(arr[0:int(len(arr) / 2)])
        rightHalf = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(leftHalf, rightHalf)

    return arr

merge_sort([8,5,6,7,10,11,15,12,5,8])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
