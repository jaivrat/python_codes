
# consist of partition first then

# This moves the pivot value to correct position
# and gives the position of pivot
# from_index, to_index inclusive
def partition(arr, from_index, to_index):
    if from_index > to_index:
        raise Exception("from_index > to_index: some logical error in the call")
    # Nothing to partition if from and to are same
    # pivot is same as well.
    if from_index == to_index:
        return from_index

    # 1. Choose first element as pivot
    pivot = arr[from_index]
    i = from_index + 1
    j = to_index

    while True:
        # increment i till you find an element > pivot
        while True:
            # if i walks beyond j, stop
            if i>j or arr[i] > pivot:
                break
            i = i + 1
    
        # decrement j till you find an element <= pivot
        while True:
            if j<i or arr[j] <= pivot:
                break
            j = j - 1

        # (a) either i and j have walked past each other, or  
        # (b)they are pointing to correct elements to be exchanged
        #(a)
        if i > j:
            # j is the position of pivot - we need to put pivot in right place
            arr[from_index], arr[j] = arr[j], arr[from_index]
            break
        #(b)
        arr[i] , arr[j] = arr[j] , arr[i]
    return j


def quick_sort(arr, start_idx, end_idx):
    # no need to sorting do nothing
    if end_idx <= start_idx:
        return
    # create partition and sort
    partition_index_at = partition(arr, start_idx, end_idx)
    quick_sort(arr, start_idx, partition_index_at)
    quick_sort(arr, partition_index_at+1, end_idx)
    return

if __name__ == '__main__':
    a = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    print("orginal" + str(a))
    quick_sort(a, 0, len(a)-1)
    print("    new" + str(a))
