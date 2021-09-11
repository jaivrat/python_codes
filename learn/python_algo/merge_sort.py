
# low_idx inclusive
# high_idx inclusive
def merge(arr, left_low, left_high, right_low, right_high):
    # holding merged array
    hold = []
    left_arr = [arr[i] for i in range(left_low, left_high+1)]
    right_arr = [arr[i] for i in range(right_low, right_high+1)]

    while len(left_arr)>0 and len(right_arr)>0:
        l = left_arr[0]
        r = right_arr[0]
        if l < r:
            hold.append(left_arr.pop(0))
        else:
            hold.append(right_arr.pop(0))

    # one of them has finished till here:
    while len(left_arr)>0:
        hold.append(left_arr.pop(0))

    while len(right_arr)>0:
        hold.append(right_arr.pop(0))

    # start filling merged values: back in arr
    for i in range(left_low, left_high+1):
        arr[i] = hold.pop(0)
    for i in range(right_low, right_high+1):
        arr[i] = hold.pop(0)


# low_idx inclusive
# high_idx inclusive
def merge_sort(arr, low_idx, high_idx):
    if low_idx < high_idx:
        mid = low_idx + int((high_idx - low_idx)/2)
        merge_sort(arr, low_idx, mid)
        merge_sort(arr, mid+1, high_idx)
        merge(arr, low_idx, mid, mid+1, high_idx)
    return

if __name__ == '__main__':
    a = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    print("original" + str(a))
    merge_sort(a, 0, len(a)-1)
    print("    new" + str(a))


