class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for num in nums:
            s[num]=s.get(num,0)+1
        ko=dict(sorted(s.items(),key=lambda x:x[1],reverse=False))
        result=list(ko.keys())[-k:]
        return result
        