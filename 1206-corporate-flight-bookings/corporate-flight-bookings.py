class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n

        for f, l, seats in bookings:
            res[f - 1] += seats
            if l < n:
                res[l] -= seats

        curr = 0
        for i in range(n):
            curr += res[i]
            res[i] =  curr
        return res            