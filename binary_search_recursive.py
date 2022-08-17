
#Binary search algo recursive approach 

def Binarysearch(data,low,high,v):
    if low<=high:

        # calculate the mid
        mid=(high+low)//2

        if data[mid]==v:
            return mid

        # if value is less then mid  then search left half
        elif data[mid]>v:
            return Binarysearch(data,low,mid-1,v) 

        # if value is grater then mid search right half
        else:
           return Binarysearch(data,mid+1,high,v)       
    else:
        return -1 





    
if __name__ == "__main__":
    data = [10,20,30,40]  # data must be sorted
    value = 20
    print(Binarysearch(data,0,len(data)-1,value))    