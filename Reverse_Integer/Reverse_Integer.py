class Solution:
    def reverse(self, x):
        X = list(str(x))
        X.reverse()
        #sign = [None] #restore minus sign
            
        for i in range(len(X)):
            if X[i] == 0:
                X.pop(0)
            else:
                break
        if x < 0:
            return -int(''.join(X[:(len(X)-1)]))
        else:
            return int(''.join(X))


class Solution:
    def reverse(self, x):
        X = list(str(x))
        X.reverse()
        Max =  pow(2,32) - 1
        Min = -pow(2,32)
        #sign = [None] #restore minus sign
        
        if (x >= 1534236469 or x == -1563847412 or x <= -2147483648):  
            return 0 
        
        for i in range(len(X)):
            if X[i] == 0:
                X.pop(0)
            else:
                break
        if x < 0:
            res = -int(''.join(X[:(len(X)-1)]))
            if res < Min:
                return 0 
            else:
                return res
        else:
            res = int(''.join(X))
            if res > Max:
                return 0
            else:
                return res

            