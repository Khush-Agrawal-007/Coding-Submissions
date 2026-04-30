class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = abs(n)
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        if n < 0:
            rev = -rev
        return abs(n - rev)