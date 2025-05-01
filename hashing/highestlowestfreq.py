def Frequency(arr, n):
    mp = {}
    current_lowest_index  = 0
    current_highest_index = 0
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
            if arr[current_highest_index] < mp[arr[i]]:
                current_highest_index = i
        else:
            mp[arr[i]] = 1
            if arr[current_lowest_index] > mp[arr[i]]:
                current_lowest_index = i
    for x in mp:
        print(x, mp[x])
    print("Current Highest",current_highest_index, arr[current_highest_index])
    print("Current Lowest",current_lowest_index, arr[current_lowest_index])


if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    Frequency(arr, n)