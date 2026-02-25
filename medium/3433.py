class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        res = [0] * numberOfUsers
        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))
        nextOnline = [0] * numberOfUsers
        allAdd = 0
        for e, t, m in events:
            t = int(t)
            if e == "MESSAGE":
                if m == "ALL":
                    allAdd += 1
                
                elif m == "HERE":
                    for i, v in enumerate(nextOnline):
                        if v <= t:
                            res[i] += 1
                else:
                    for idx in m.split():
                        res[int(idx[2:])] += 1

            else:
                nextOnline[int(m)] = t + 60

        if allAdd:
            for i in range(numberOfUsers):
                res[i] += allAdd
        return res
