class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        /* Lazy Way
        a = eval("0b" + a)
        b = eval("0b" + b)
        */
        '''
        new_a = 0
        new_b = 0
        
        for i in range(1, len(a) + 1):
            print(a[-i], i)
            new_a += int(a[-i]) * (2 ** (i - 1))
        for i in range(1, len(b) + 1):
            new_b += int(b[-i]) * (2 ** (i - 1))

        print(new_a, new_b)
        return str(bin(new_a + new_b))[2:]
