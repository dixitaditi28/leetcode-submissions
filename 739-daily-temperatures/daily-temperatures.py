class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack = []

        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                past_d = stack.pop()
                res[past_d] = i - past_d
            stack.append(i)
        return res        