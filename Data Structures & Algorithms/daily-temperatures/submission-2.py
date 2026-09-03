class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

###we can use Monotonic Decreasing Stack because stack will have decresing temperature indices


        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result 






        
        