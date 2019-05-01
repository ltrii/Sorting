# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    hold1 = 0
    hold2 = 0
    for i in range(elements):
        if hold1 >= len(arrA):
            merged_arr[i] = arrB[hold2]
            hold2 += 1
        elif hold2 >= len(arrB):
            merged_arr[i] = arrA[hold1]
            hold1 += 1
        elif arrA[hold1] < arrB[hold2]:
            merged_arr[i] = arrA[hold1]
            hold1 += 1
        else:
            merged_arr[i] = arrB[hold2]
            hold2 += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        cutpoint = int(len(arr)/2)
        leftHalf = merge_sort(arr[:cutpoint])
        rightHalf = merge_sort(arr[cutpoint:])
        arr = merge(leftHalf, rightHalf)

    return arr

print(merge_sort([8,5,7,3,2,9]))

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
