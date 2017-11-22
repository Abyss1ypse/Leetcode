class Solution: # Wrong one 
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        
        map = {}
        start = end = 0
        
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = i
            else:
                if i-map[s[i]] > end - start:
                    start = map[s[i]]
                    end = i
                #map[s[i]] = i

        return s[start:end+1]
                

class Solution: # Too slow
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        
        res = ""
        for i in range(len(s)):
            l_odd = i
            r_odd = i
            while l_odd >= 0 and r_odd <= len(s) - 1 and s[l_odd] == s[r_odd]:
                tmp = s[l_odd:r_odd+1]
                l_odd += - 1
                r_odd += 1
                
            if len(tmp) > len(res):
                res = tmp
                
            l_even = i
            r_even = i + 1
            while l_even >= 0 and r_even <= len(s) - 1 and s[l_even] == s[r_even]:
                tmp = s[l_even:r_even+1]
                l_even += - 1
                r_even += 1
                
            if len(tmp) > len(res):
                res = tmp
        return res


class Solution: 
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        
        res = ""
        for i in range(len(s)):
            # res = max(self.Tester(s,i,i), self.Tester(s,i,i+1), res, key=len)
            tmp = self.Tester(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.Tester(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    def Tester(self,s,l,r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l += - 1
                r += 1
        return s[l+1:r]
        