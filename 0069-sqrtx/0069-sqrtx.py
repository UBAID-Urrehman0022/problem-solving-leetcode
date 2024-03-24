class Solution:
    def mySqrt(self, x: int) -> int:
        
        l , r = 0,x//2
        res = 0
        while (l<=r):
            mid = l+ (r-l)//2
            if mid*mid < x:
                l= mid+1
                res = mid
            elif mid* mid > x:
                r = mid-1
            else:
                return mid
        if x==1:
            return 1  
        return res
        
                
        
       
