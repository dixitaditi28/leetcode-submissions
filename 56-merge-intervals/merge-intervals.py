class Solution:
    def merge(self, intv: List[List[int]]) -> List[List[int]]:
        if not intv:
            return[]

        intv.sort(key=lambda x: x[0])
        mrgd = [intv[0]]

        for s, e in intv[1: ]:
            if s <= mrgd[-1][1]:
                mrgd[-1][1] = max(mrgd[-1][1], e)
            else:
                mrgd.append([s, e])
        return mrgd            
