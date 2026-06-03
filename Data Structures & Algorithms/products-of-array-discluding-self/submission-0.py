class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        preproduct=1
        postproduct=1
        l =[1]*n
        for i in range(n):
            l[i]*=preproduct
            preproduct*=nums[i]
            l[n-i-1]*=postproduct
            postproduct*=nums[n-i-1]
        return l

        