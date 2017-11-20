class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        s = [None]*(m+n)
        i = j = 0
        
        for k in range(m+n):
            if i > n - 1: #nums1 is empty, copy the rest of nums2 to result
                s[k:] = nums2[j:]
                break
            if j > m - 1: #nums2 is empty, copy the rest of nums1 to result
                s[k:] = nums1[i:]
                break
            
            if nums1[i] < nums2[j]:
                s[k] = nums1[i]
                i = i+1
            else:
                s[k] = nums2[j]
                j = j+1
                
        if (n+m)%2 == 1:
            return float(s[(m+n)//2])
        else:
            return float((s[(m+n)//2] + s[-1 + (m+n)//2])/2)
    
        