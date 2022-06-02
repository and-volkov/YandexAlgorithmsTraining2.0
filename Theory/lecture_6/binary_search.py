def l_binary_search(left, right, check, check_params):
    while left < right:
        mid = (left + right) // 2
        if check(mid, check_params):
            right = mid
        else:
            left = mid + 1
    return left


def r_binary_search(left, right, check, check_params):
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, check_params):
            left = mid
        else:
            right = mid - 1
    return right
