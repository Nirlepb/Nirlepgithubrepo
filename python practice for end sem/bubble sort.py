#bubble sort 
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        #for repeting number of times
        for j in range(0,n-i-1):
            #
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
data=[2,54,6,7,89,9]
print(bubblesort(data))            