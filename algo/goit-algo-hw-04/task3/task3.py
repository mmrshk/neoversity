# Insertion sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Timsort
def insertion_sort_range(lst, lo, hi):
    for i in range(lo + 1, hi):
        key = lst[i]
        j = i - 1
        while j >= lo and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def _reverse_range(lst, lo, hi):
    hi -= 1
    while lo < hi:
        lst[lo], lst[hi] = lst[hi], lst[lo]
        lo += 1
        hi -= 1


def _calc_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def _merge_adjacent(arr, lo, mid, hi):
    merged = merge(arr[lo:mid], arr[mid:hi])
    arr[lo:hi] = merged


def tim_sort(arr):
    n = len(arr)
    if n < 2:
        return arr

    min_run = _calc_min_run(n)
    runs = []
    i = 0
    while i < n:
        run_end = i + 1
        if run_end < n:
            if arr[run_end - 1] <= arr[run_end]:
                while run_end < n and arr[run_end - 1] <= arr[run_end]:
                    run_end += 1
            else:
                while run_end < n and arr[run_end - 1] > arr[run_end]:
                    run_end += 1
                _reverse_range(arr, i, run_end)

        if run_end - i < min_run:
            run_end = min(i + min_run, n)
            insertion_sort_range(arr, i, run_end)

        runs.append(run_end)
        i = run_end

    while len(runs) > 1:
        new_runs = []
        lo = 0
        idx = 0
        while idx < len(runs):
            if idx + 1 < len(runs):
                mid = runs[idx]
                hi = runs[idx + 1]
                _merge_adjacent(arr, lo, mid, hi)
                new_runs.append(hi)
                lo = hi
                idx += 2
            else:
                new_runs.append(runs[idx])
                idx += 1
        runs = new_runs

    return arr
