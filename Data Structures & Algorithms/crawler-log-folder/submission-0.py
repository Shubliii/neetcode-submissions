class Solution:
    def minOperations(self, logs: List[str]) -> int:

        depth=0

        for c in logs:   ##range(0, len(logs)) 0 ,1 ,2 ,3... number generate karega 

            if c=="../":
                if depth>0:
                    depth -=1
            elif c=="./":
                continue
            else:
                depth +=1

        return depth                





        