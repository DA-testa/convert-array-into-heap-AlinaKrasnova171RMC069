# python3
import os

def build_heap(data):
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        checkin(data, n, i, swaps)
    return swaps

#corresponding checks
def checkin(data, n, i, swaps) :
    index = i
    right = i*2 + 2
    left = i*2 + 1

    if right < n and data[right] < data[index]:
        index = right
    if left < n and data[left] < data[index]:
        index = left
    if i != index:
        swaps.append((i,index))
        data[i], data[index] = data[index], data[i]
        checkin(data, n, index, swaps)


def main():
    
    # TODO : add input 
    # add another input for I or F 
    imp = input() # first two tests are from keyboard, third test is from a file

    if "F" in imp:
        path = './tests/'
        file = input()
        folder = path + file
        
        #test_path = path + test_file
        with open(folder, "r") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    

    if "I" in imp:
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
