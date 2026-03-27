def find(search_list, value):
    if not value in search_list:
        raise ValueError("value not in array")
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if search_list[mid] == value:
            return mid
        elif value > search_list[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1