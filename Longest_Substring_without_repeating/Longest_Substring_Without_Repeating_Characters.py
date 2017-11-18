class Solution:
    def lengthOfLongestSubstring(self, s):       
        if len(s) == 0:
            return 0 
        start = 0
        n = 1
        map = {}
        map[s[0]] = 0
        for i in range(1,len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]]+1
            else:             
                n = max(n,i-start+1)
            map[s[i]] = i
        return n

# Answer
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength