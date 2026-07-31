def find(search_list, value):
    length = len(search_list)
    if length == 0 or value < search_list[0] or value > search_list[-1]:
        raise ValueError("value not in array")
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] < value:
            left = mid + 1
        elif search_list[mid] > value:
            right = mid - 1
        else:
            return mid
    raise ValueError("value not in array")
