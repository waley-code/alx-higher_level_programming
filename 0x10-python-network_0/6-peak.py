def find_peak(arr):
    """
    Returns the peak element in the given array
    """
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1
            
    return arr[low]
