class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        array = []
        for i in range(length):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                array.append(s[i])
            elif len(array)!=0 and s[i] == ")":
                if array[-1] == "(":
                    array.pop()
                else:
                    return False
            elif len(array)!=0 and s[i] == "]":
                if array[-1] == "[":
                    array.pop()
                else:
                    return False
            elif len(array)!=0 and s[i] == "}":
                if array[-1] == "{":
                    array.pop()
                else:
                    return False
            else:
                array.append(s[i])
        if len(array) == 0:
            return True
        else:
            return False
            
                
        # for i in range(len(s)//2):
        #     if s[i] == "(" and s[length-i-1] == ")":
        #         continue
        #     elif s[i] == "[" and s[length-i-1] == "]":
        #         continue
        #     elif s[i] == "{" and s[length-i-1] == "}":
        #         continue
        #     else:
        #         return False
        # return True