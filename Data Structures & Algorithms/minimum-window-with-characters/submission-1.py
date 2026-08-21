class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()

        left = 0
        have = 0
        ans = ""

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == len(need):
                current = s[left:right + 1]

                if ans == "" or len(current) < len(ans):
                    ans = current

                c = s[left]
                window[c] -= 1

                if c in need and window[c] < need[c]:
                    have -= 1

                left += 1

        return ans