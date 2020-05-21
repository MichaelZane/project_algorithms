'''
Input: an integer
Returns: an integer
caching/memoization: save your work so you can access it and not repeat yourself

'''
'''
need some sort of data structure: arrays and dict
if we check our cache and see the answer is there, just return our answer
how do answers get there?
first time calculating an answer, were are going to save it
'''
#caching make this now O(n) extra memory though
def eating_cookies(n, cache=None):                                            # 3 choices always
    #set the base case to when there asre no more cookies this is O(3^n) runtime
    if n == 0:
        return 1
    elif n < 0:
        return 0
#init our cache if we dont have it yet
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            #cache = {i: 0 for i in range(n+1)}
            cache = [0 for _ in range(n+1)]
            #we can save it now
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]
        #


    

print(eating_cookies(5))   
    
    
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
