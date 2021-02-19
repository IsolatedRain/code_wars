def pick_peaks(arr):
    res = {"pos": [], "peaks": []}
    n = len(arr)
    pID = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            pID = i
        elif arr[i] < arr[i - 1] and pID != 0:
            if arr[i - 1] == arr[pID]:
                res["pos"].append(pID)
                res["peaks"].append(arr[pID])
    return res


# arr = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]
# arr = [2, 1, 3, 1, 2, 2, 2, 2, 1]
# arr = [2, 1, 3, 1, 2, 2, 2, 2]
# arr = [1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]
arr = [10, 10, 8, 4, 18, 1, -4, -4, 9, 10, 3, 19, 17, 18, 13, 19, -3, 2, 14, -4, 0, 16, 2, 10, 6]
print(pick_peaks(arr))
