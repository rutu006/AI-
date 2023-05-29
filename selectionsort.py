def selectionsort(arr,n):
    for i in range(n):
        minindex = i
        for j in range(i+1,n):
            if(arr[j] < arr[minindex]):
                minindex = j
        arr[i],arr[minindex] = arr[minindex],arr[i]
    return arr
def printarr(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
def main():
    n = int(input("Enter number of elements in array u want to insert : "))
    arr = []
    for i in range(0,n):
        k = int(input("Enter element :"))
        arr.append(k)
    print("ARRAY BEFORE SORTING : ",printarr(arr,n))
    selectionsort(arr,n)
    print("ARRAY AFTER SORTING : ",printarr(arr,n))
    
if __name__ =='__main__':
    main()
