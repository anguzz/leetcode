#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        counter=0
        
        for i in nums:
            if (i-1) not in numSet: #if no left neighbor
                seq=0               #not sequence so = 0 
                while (i+seq) in numSet:    #while currnumber + sequence is in set
                    seq +=1                 #increment sequence 
                counter=max(seq,counter)    #get max sequence so far
        return counter
                
  






    '''
    NOTES
-not allowed to use sort, since asks for O(n) time solution and sort makes it O(logn)
if we sorted we would just count longest increasing sequence starting at start 


-instead we iterate through array, use a set, check if value has left neighbors, if not they are seq starts,
then increment for every increasing value found in our set

take example 
[100, 4, 200, 1, 3, 2]

-100,look for n-1= 99 dne so is seq start
check if 101 in set, does not,end counter w/ 0

-4,look for n-1, 3 exist in set so not seq start

-200,199 dne, so is seq start
check if 201 in set, does not,end counter w/ 0

-1,look for n-1=0, dne so is sequence start, increase seq counter 
check if 2 in set does, increase seq counter
check if 3 in set, does, increase seq counter 
check if 4 in set, does,increase seq counter
save curr max sequence in counter


-3,  2 exist in set so not seq start

-2, 1 exist in set so not seq start

end of loop.
    '''


        
