# number of ways to sum up to 'N' 
def countWays(arr,N): 
  
    count = [0 for i in range(N + 1)] 
      
    # base case 
    count[0] = 1
      
    # Count ways for all values up  
    # to 'N' and store the result 
    for i in range(1, N + 1): 
        for j in range(len(arr)): 
  
            # if i >= arr[j] then 
            # accumulate count for value 'i' as 
            # ways to form value 'i-arr[j]' 
            if (i >= arr[j]): 
                count[i] += count[i - arr[j]] 
                print(i,arr[j])
      
    # required number of ways  
    return count[N]
      
# Driver Code 
#arr = [32973, 33033, 33952,32873,92470,34606,5000,28991,17975] 
arr=[1,2]
#N = 86572
N=6
answer=countWays(arr,N) 
print(answer)   