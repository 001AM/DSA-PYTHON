
def merge(left,right):
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    else:
        result += right
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)

        # Merge the sorted halves
        return merge(left_sorted,right_sorted)


if __name__ == '__main__':
    arr = [38, 27, 43, 10]
    merge_sort(arr)
    print(arr)  # Print the sorted array