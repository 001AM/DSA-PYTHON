def selection_sort(arr, n=None):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", arr)
selection_sort(arr)
print("After sorting:", arr)
