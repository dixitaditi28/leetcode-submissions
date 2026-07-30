class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)

        bound = set()

        for s, e, color in segments:
            diff[s] += color
            diff[e] -= color
            bound.add(s)
            bound.add(e)

        res = []
        curr_color = 0
        prev_bound = -1

        for b in sorted(bound):
            if curr_color > 0:
                res.append([prev_bound, b, curr_color])

            curr_color += diff[b]
            prev_bound = b
        return res            