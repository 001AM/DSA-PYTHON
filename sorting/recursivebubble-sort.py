def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    # Base case: If the array size is 1, return
    if n == 1:
        return arr
    # One pass of bubble sort. After this pass, the largest element is moved to end.
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # Recursive call for the remaining array
    return bubble_sort(arr, n - 1)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", arr)
bubble_sort(arr)
print("After sorting:", arr)
