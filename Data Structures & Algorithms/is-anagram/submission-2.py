class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1
        for val in count:
            if val!= 0:
                return False
        return True
        
        ### Sol_1
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # for i,j in zip(s,t):
        #     if i!=j:
        #         return False
        # if len(s)!=len(t):
        #     return False
        # else:
        #     return True
            