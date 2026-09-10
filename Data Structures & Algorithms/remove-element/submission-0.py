class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result=[]
        n=len(nums)
        for num in nums:
            if val==num:
                continue
            result.append(num)
        for i in range(len(result)):
            nums[i]=result[i]
        
        return len(result)
        