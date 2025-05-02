def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [2,0 , 2, 3, 1, 4]
print("Before sorting:", arr)
print("After sorting:", insertion_sort(arr))
