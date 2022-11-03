
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0 
        curr_min=prices[0] 
        
        for i in range(len(prices)):
            if prices[i]<curr_min:   
                curr_min=prices[i]   
            else:
                profit=prices[i]-curr_min  #curr profit is (current price - min stock)
                maxP=max(maxP,profit)    #compare our max profit and curr profit, reassign
        return maxP

    
    #first if is to find lowest priced day
    #second else just check all days against that min and choose one nets biggest num(stock)
