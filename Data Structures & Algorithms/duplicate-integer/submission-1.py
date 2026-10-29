class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for num in nums:
            s.add(num)
        print(s)
        if len(s)==len(nums):
            return False
        else:
            return True


        