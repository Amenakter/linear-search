class Solution:

	
	def search(self,arr, k):
	    
	    for i in range(len(arr)):
	        if arr[i]==k:
	            print("k = 7 is found in the given array at position :",i)
	            break
	    else:
	        print("value is not found")
	        
arr = [9, 7, 2, 16, 4]
k = 7
ob = Solution()
ans =ob.search(arr, k)


def linear_search(array, n):
    for i in range(len(array)):
        if array[i]==n:
            print("n =",n,"is found in the given array at position :",i)
            break
    else:
            print("n =",n,"is not found")
array = [21, 23, 45, 56, 7,6]
n = 34
linear_search(array, n)     


def search(arr, n, x):
 
    for location in range(0, n):
        if (arr[location] == x):
            return location
    return -1
 
 

arr = [2, 3, 4, 10, 40]
x = 3
n = len(arr)
 
# Function call
result = search(arr, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)


   

