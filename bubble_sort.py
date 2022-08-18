# Bubble sort algo

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):

            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

if __name__ == "__main__":
    data = [5, 2, 7, 1]
    sorted_data = bubble_sort(data)
    print(sorted_data)
  