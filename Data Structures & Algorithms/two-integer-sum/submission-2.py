class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        s={}
        for i in range(len(nums)):#1
            rem=target-nums[i]#3
            if rem in s:
                result.append(s[rem])
                result.append(i)
            s[nums[i]]=i#{3:0,4:1,5:2,6:3}

        print(s)
        print(result)
        return result



        