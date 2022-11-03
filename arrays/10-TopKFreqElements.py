class Solution:  # Time: O(N) and Space: O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                                 #dict to count times a number occurs
        freq = [[] for i in range(len(nums) + 1)]  # make freq arrays size of n 

        for num in nums:                          #iter through list
            count[num] = 1 + count.get(num, 0)    #count each numbers occurances, if doesnt occur in dict return zero       
       
        for num, count in count.items():            #iter through each key value pair   
            freq[count].append(num)                 #append each number n, to c value of times

        res = []
        for i in range(len(freq) - 1, 0, -1):      # iterate backwards, ignore zero values
            for j in freq[i]:                      # checking what's the num value at that index
                res.append(j)
                if len(res) == k:                  # return res when equal to k
                    return res
    
   
  """
      
    #======================SOLUTION 2======================
        #intuitive solution using heap
        #Iterate through nums and create hash map to store elements frequency then pop 
            
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)
            
        #Turn hash map to list with tuples(-values,keys) 
        #-values will reverse order during heapify()
        freqList = []
        for key,value in hashMap.items():
            freqList.append((-value,key))

        #Create a min-heap from list negative values 
        #since values are negative the result is a "max-heap" of needed values to keys
        heapq.heapify(freqList)

        # Create list and append keys from min-heap in inverted "max-heap" values
        res = []
        while len(res) < k:
            pop = heapq.heappop(freqList)
            res.append(pop[1]) #append key from tuple (-value,key)
			
        return res

    #======================SOLUTION 3======================
    #if allowed to use collections             
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:                 
      counter = Counter(nums).most_common()  
      return [counter[i][0] for i in range(k)]
        
 """
