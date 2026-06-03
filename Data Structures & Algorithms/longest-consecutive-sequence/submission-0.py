class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0
        s = set(nums)
        for i in s:
            if i-1 not in s:
                l=1
                while i+l in s:
                    l+=1
                long=max(long,l)
        return long