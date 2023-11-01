class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,n
        rows = 0
        while (l<=r):
            mid = l+ (r-l)//2

            coins = mid/2 * (mid+1)
            if coins > n:
                r = mid-1
            else:
                l = mid +1
                rows = max(rows, mid)
        return rows
