class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                s = nums[l]+nums[i]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    k.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return k
        