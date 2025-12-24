def selection_sort(arr):
    for i in range(len(arr)):
        #check len of data and repeat loop for that many times
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
data=[0,78,88,56,44,33,22,11]
print(selection_sort(data))