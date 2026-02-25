class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_, t_ = [], []

        for c in s:  
            if c == '#':
                if s_:
                    s_.pop()
            else:
                s_.append(c)
        
        for c in t:
            if c == "#":
                if t_:
                    t_.pop()
            else:
                t_.append(c)

        return s_ == t_
