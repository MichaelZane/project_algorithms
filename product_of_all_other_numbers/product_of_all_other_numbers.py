'''
Input: a List of integers
Returns: a List of integers
Write a function that receives an array of integers and returns an array 
consisting of the product of all numbers in the array except the number 
at that index.
'''
def product_of_all_other_numbers(arr):
    #take in an array of ints arr
    #multiply other numbers except the number at the index [1-> 7*3*4]
    #append it to new array
    #if it is 0 or 1, do not multiply
    nums_arr = []
    result = 1
    for i in range(1, len(arr)):
        while i < len(arr) - 1:
            if arr[i] <= 1:
                i += 1            
            else:
                result = arr[i] * result           
                i += 1
                
                if i > 0:
                    result2 = result * arr[i]                    i += 1
                else:
                    nums_arr.append(result2)    
                      
        return nums_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
