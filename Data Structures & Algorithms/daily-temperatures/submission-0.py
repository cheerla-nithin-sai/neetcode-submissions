class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l = []
        for i in range(len(temp)):
            for j in range(i,len(temp)):
                k = []
                if temp[j]>temp[i]:
                    k.append(j-i)
                    break
            if len(k):
                l.append(k[0])
            else:
                l.append(0)

        return l
                