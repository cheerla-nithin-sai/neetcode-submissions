class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l = [0]*len(temp)
        s = []
        for i,j in enumerate(temp):
            while s and temp[s[-1]]<j:
                idx = s.pop()
                l[idx]=i-idx
            s.append(i)
        return l
                