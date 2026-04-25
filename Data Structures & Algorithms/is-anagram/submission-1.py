class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i,j in zip(s,t):
            if i!=j:
                return False
        if len(s)!=len(t):
            return False
        else:
            return True
            