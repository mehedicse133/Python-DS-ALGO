# Implement linear secarch algo

# define a function that takes tow parameter
# First paramete is a list 
# Sencond is item, which item we are looking for in the input list


def linear_searech(data, item):
    for i in range(0,len(data)):
        if data[i] == item:
            print('Item index number :', i)

            # if item in the list then return 1
            return 1

    # if item not in the list then return -1
    return -1


if __name__ == "__main__":
    data = [20,30,40,50,60,70] 
    item = int(input('Ente a value which you want to search in list :'))
    print(linear_searech(data, item)) 


    



