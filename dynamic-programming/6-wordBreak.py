class Solution:
    def wordBreak(self, string, wordDict):

        # Tracker will be used to determine if we have successfully created a string ending at tracker[index]
        # We initialize it to all False, then set the tracker[0] to True as a base case.
        tracker = [False] * (len(string)+1)
        tracker[0] = True

        # Outer loop will be ahead of inner loop at all times.
        for right in range(1, len(string)+1):
            
            # Inner loop will start at string[0] and increment up to right, checking each time to see if string[left:right] is in wordDict
            for left in range(right):

                # tracker[left] tells us if we have successfully created a word up to that index.
                # Checking tracker[left] helps us ensure that we're only marking tracker True when words are adjacent.
                if tracker[left] and string[left:right] in wordDict:

                    # Update our tracker to show that we have created adjacent word(s) up to index `right`
                    # For example, if string=`catdog` and left=0 and right=3, then string[left:right] is 'cat'.  
                    # So tracker[right] becomes True, giving us tracker=[True, False, False, True, False, False, False].
                    tracker[right] = True

                    # Using break lets us return to the outer loop, incrementing `right` to see if we can create a word
                    # farther down the line in string
                    break
        
        # After we have incremented right through all of string, returning tracker's last index tells us whether we were able 
        # to reach the end of str with adjacent words, and tells us whether the very last character was included in one of those words
        return tracker[-1]
