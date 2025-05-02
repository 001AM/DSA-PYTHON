def quick_sort(sequence):
    length = len(sequence)
    if length < 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Example usage:
arr = [5,6,7,8,9,8,7,6,5,6,7,8,9,0]
print("Before sorting:", arr)
print("After sorting:", quick_sort(arr))
