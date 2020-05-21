'''
Input: a List of integers
Returns: a List of integers
Write a function that takes an array of integers and moves each 
non-zero integer to the left side of the array, then returns the altered array.
The order of the non-zero integers does not matter in the mutated array.
while index < len(my_list):
	# Do something to my_list[index]
	index += 1
'''

def moving_zeroes(arr):
    
    print(arr)
    i = 0
    while i < len(arr):        
        if arr[i] is 0:
            arr.append(arr[i])
            arr.remove(arr[i])
            i += 1
            print(arr)
        else:
            i += 1
            print(arr)
        
    return arr
    # iterate and move the non zero's right, zero's to right
    
    
            
    
    
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")