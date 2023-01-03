class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        s = strs
        for i in range(len(s[1])):
            t = []
            for j in range(len(s)):
                t.append(s[j][i])
            if t != sorted(t):
                count += 1
        return count
                
