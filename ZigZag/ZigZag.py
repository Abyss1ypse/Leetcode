class Solution:
    def convert(self, s, numRows):

        if len(s) == 0 or numRows == 1:
            return s
        
        T = 2 * numRows - 2
        Z = ["" for i in range(numRows)]
        map = {}
        # map = {i:i if i<nRows else (period-i) for i in xrange(period)}
        for i in range(T):
            if i < numRows:
                map[i] = i
            else:
                map[i] = T - i
                
        for i in range(len(s)):
            Z[map[i%T]] += s[i]
            
        return "".join(Z)
            
