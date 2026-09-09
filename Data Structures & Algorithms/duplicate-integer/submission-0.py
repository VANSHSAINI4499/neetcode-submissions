class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result=set()
        s=False
        for i in range(len(nums)):
            if nums[i] in result:
                s=True
            result.add(nums[i])
        print(result)
        return s

        