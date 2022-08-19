# Selection sort algo

def selection_sort(data):
    for i in range(len(data)):
        small_index = i

        for j in range(i+1,len(data)):
            if data[small_index]>data[j]:
                small_index = j

        data[i], data[small_index] = data[small_index], data[i]    

    return data

if __name__ == "__main__":
    data = [5,1,6,2,7] 
    sorted_data = selection_sort(data)
    print(sorted_data)