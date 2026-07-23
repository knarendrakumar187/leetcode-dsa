class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        while(i<n):
            correct = nums[i]
            if(nums[i]<n and nums[i]!= nums[correct]):
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i=i+1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return nums[i]
        return -1


        