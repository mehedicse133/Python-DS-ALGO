
#Binary search algo recursive approach 

def binary_search_recursive(data,low,high,item):
    if low<=high:

        # calculate the mid
        mid=(high+low)//2

        if data[mid]==item:
            return mid

        # if value is less then mid  then search left half
        elif data[mid]>item:
            return binary_search_recursive(data,low,mid-1,item) 

        # if value is grater then mid search right half
        else:
           return binary_search_recursive(data,mid+1,high,item)       
    else:
        return -1 








if __name__ == "__main__":
    data = [10,20,30,40]  # data must be sorted
    search_item = 40
    result = binary_search_recursive(data,0,len(data)-1,search_item)
    if result == -1:
        print('Item not present in the list') 
    else:     
        print(f'Item found {result}'+'th' + ' ' +'index in the list')
     