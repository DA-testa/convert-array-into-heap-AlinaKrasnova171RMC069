# python3
import os

def build_heap(arr):
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    swaps = []
    n = len(arr)

    for i in range(n // 2, -1, -1):
       
        #corresponding checks

        index = i
        right = i*2 + 2
        left = i*2 + 1


        if right < n and arr[right] < arr[index]:
            index = right
        if left < n and arr[left] < arr[index]:
            index = left
        if i != index:
            swaps.append((i,index))
            arr[i], arr[index] = arr[index], arr[i]
            
        while True:
            i = index 
            right = i*2 + 2
            left = i*2 + 1

            if right < n and arr[right] < arr[index]:
                index = right
            if left < n and arr[left] < arr[index]:
                index = left
            if i == index:
                break

            swaps.append((i,index))
            arr[i], arr[index] = arr[index], arr[i]
            
        
    return swaps



def main():
    
    # TODO : add input 
    # add another input for I or F 
    imp = input() # first two tests are from keyboard, third test is from a file

    if "F" in imp:
        path = "./tests/"
        file = input()
        file_path = path + file
        if "a" not in file:
            try:
                with open(file_path) as fl:
                    n = int(fl.readline())
                    arr = list(map(int, fl.readline().split()))
            except FileNotFoundError:
                print("Error: file not found ")
                return

        else:
            print("Error")
        
        
    

    if "I" in imp:
    # input from keyboard
        n = int(input())
        arr = list(map(int, input().split()))
    
    # checks if lenght of data is the same as the said lenght
    assert len(arr) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(arr)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n*4

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
