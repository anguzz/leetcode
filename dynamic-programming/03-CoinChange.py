class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxA = amount+1            #0->amount
        mincoins = [maxA] * (maxA) #create array full of default max(curr target)   
        mincoins[0] = 0            #base case 0 coins
    
        for coin in coins:          
            for target in range(1, maxA): 
                if coin <= target:    
                    mincoins[target] = min(mincoins[target], mincoins[target-coin] + 1)	
        return mincoins[amount] if mincoins[amount] != maxA else -1
