

# Binary search iterative approach
def binary_search_iterative(data, search_item):
    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if data[mid] == search_item:
            return mid

        elif data[mid] < search_item:
            low = mid + 1

        else:
            high = mid - 1
    return -1


data = [10, 20, 30, 40]
item = 11
print(binary_search_iterative(data, item))   