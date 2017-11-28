class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        
        base = 1
        while x/base >= 10:
            base *= 10
        
        while x:
            left  = x // base 
            right = x % 10
            if left != right:
                return False
            
            x = (x % base)//10
            base /= 100 
        return True