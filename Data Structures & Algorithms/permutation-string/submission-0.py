class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        m=len(s2)
        n=len(s1)
        r=n
        while r<=m:
            if sorted(s1) == sorted(s2[l:r]):
                return True
            r+=1
            l+=1
        return False