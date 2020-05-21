'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
arrays are not the nest structures are not the best to be searched through
what are other data structures that can be searched?
dictionaries are the best to be searched
'''
def single_number(arr):
    i = 0
    #iterate over arr and find the elements match that does have a match
    for i in range(len(arr)):
        #init var for pairs
        pairs = False
        for j in range(len(arr)):
        #find matching pairs 
            if i != j and arr[i] == arr[j]:
                pairs = True
        #break and return when not a pair
        if not pairs:
            return arr[i]
        
    return
    
    #this is O(n^2)
    # no_dups = []
    
    # for x in arr:  O(n)
    #     if not x not in no_dups:   O(n)
    #         no_dups.append(x)
    #         no_dups.remove(x)     O(n)
     
    # return no_dups[0]            
# O(2 * n) or O(n)           
# def single_number(nums):
#     counts = {}
    
#     #loop through nums to tally up how many times weve seen the number
#     # O(n)
#     for x in nums:
#         if x in counts:         # O(1)
#             counts[x] == 1
#         else:
#             counts[x] = 1 
        
#     #loop through all of the key-value pairs in counts to find the one pair with a value of 1
#     # O(n)
#     for num in counts:
#         if counts[num] == 1:
#             return num 
        
# def single_number(nums):          
    
#     counts = {}
    
#     #loop through nums to tally up how many times weve seen the number
#     # O(n)
#     for x in nums:
#         if x in counts:         # O(1)
#             del counts[x]
#         else:
#             counts[x] = 1 
        
#     #loop through all of the key-value pairs in counts to find the one pair with a value of 1
#     # O(n) so single entry makes it O(1)
#     for num in counts:
#         if counts[num] == 1:
#             return num 
        
                 


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f'The odd-number-out is {single_number(arr)}')