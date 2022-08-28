# implement insertion sort
def insertion_sort(list):

    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
                
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
            
        list[j + 1] = key
        
    return list

if __name__ == "__main__":
    list = [9, 8, 6, 7, 1]
    sorted_list = insertion_sort(list)
    print(sorted_list)