# binary search funtion find item in an sorted list

def binary_search(arr,x):
    l = 0
    h = len(arr)
    while l<=h :
        mid = (l+h)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            h = mid-1
        else:
            return mid
    return -1

