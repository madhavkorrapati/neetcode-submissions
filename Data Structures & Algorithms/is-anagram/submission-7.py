class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ten=len(t)
        sen=len(s)
        if sen==ten:
            return Counter(s) == Counter(t)
        return False