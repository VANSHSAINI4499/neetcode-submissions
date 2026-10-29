class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result1={}
        result2={}
        for i in s:
            result1[i]=result1.get(i,0)+1
        print(result1)
        for i in t:
            result2[i]=result2.get(i,0)+1
        print(result2)
        if result1==result2:
            return True
        return False
            

        