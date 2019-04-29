# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for w in range(cur_index, len(arr)):
            if arr[w] < arr[smallest_index]:
                smallest_index = w
        # TO-DO: swap
        swap = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = swap

    return arr

print(selection_sort([8,7,10,19,2,22,24,3]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaper = True
    while swaper:
        swaper = False
        for i in range(0, len(arr) - 1):
            bubble1 = arr[i]
            bubble2 = arr[i+1]
            if bubble1 > bubble2:
                arr[i] = bubble2
                arr[i+1] = bubble1
                swaper = True
    return arr

print(bubble_sort([8,7,10,19,2,22,24,3]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    max_val = max(arr)
    counting = [0] * (max_val + 1)
    for i in range(0,len(counting)):
        for p in range(0,len(arr)-1):
            if i == arr[p]:
                counting[i] += 1
    return counting

print(count_sort([1,5,3,3,3,3,10,10,10,6,4,9,2]))