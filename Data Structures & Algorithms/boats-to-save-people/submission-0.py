
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        p1 = 0
        p2 = len(people) - 1
        count = 0

        while p1 <= p2:
            x = people[p1] + people[p2]

            if x <= limit:
                p1 += 1

            p2 -= 1
            count += 1

        return count

                





        
        