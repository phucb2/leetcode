# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/?envType=daily-question&envId=2023-09-12
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        freq = sorted(counter.values(), reverse=True)
        
        ans = 0
        for i in range(1, len(freq)):
            if freq[i - 1] <= freq[i]:
                ans += min(freq[i] - (freq[i - 1] - 1), freq[i])
                freq[i] = max(0, freq[i - 1] - 1)
        return ans
