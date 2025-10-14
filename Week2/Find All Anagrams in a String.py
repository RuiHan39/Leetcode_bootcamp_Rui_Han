class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        ans = []
        contain = collections.Counter()
        for i in range(len(p)):
            contain[p[i]]+=1
        window = len(p)
        j = 0
        subcontain = collections.Counter()
        for i in range(window):
            subcontain[s[i]] +=1
        while j <= len(s)-len(p):
            if subcontain == contain:
                ans.append(j)
            if j == len(s) -len(p):
                break
            else:
                subcontain[s[j]] -= 1
                subcontain[s[j+window]] += 1
                j += 1

        return ans
