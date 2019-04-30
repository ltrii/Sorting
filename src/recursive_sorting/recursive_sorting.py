# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    r = 0
    s = 0
    for i in range(elements):
        if r >= len(arrA):
            merged_arr[i] = arrB[s]
            s += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        leftHalf = merge_sort(arr[0:len(arr)/2])
        rightHalf = merge_sort(arr[len(arr)/2:])
        arr = merge(leftHalf, rightHalf)

    return arr

print(merge_sort([5,1,9,3,4]))

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
