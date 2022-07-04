def quick_sort(list_):
    if len(list_) < 2:
        return list_
    pivot = list_[0]
    left_list = quick_sort([e for e in list_ if e < pivot])
    mid_list = [e for e in list_ if e == pivot]
    right_list = quick_sort([e for e in list_ if e > pivot])
    return left_list + mid_list + right_list
    



assert quick_sort([]) == []
assert quick_sort([7]) == [7]
assert quick_sort([1,2]) == [1,2]
assert quick_sort([2,2]) == [2,2]
assert quick_sort([2,1]) == [1,2]
assert quick_sort([2,1, 7, 11, 11, 1, 0, -1, 18]) == [-1, 0, 1, 1, 2, 7, 11, 11, 18]
