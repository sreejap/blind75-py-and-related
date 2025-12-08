class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int (a,2)
        y = int (b,2)
        # LC tip: How to start? There is an interview tip for bit manipulation problems: if you don't know how to start, start by computing XOR for your input data. 
        while y:
            answer = x ^ y # answer is x xor y
            carry = (x&y) << 1 # compute carry by doing & of x,y and left shift bits by 1
            x = answer
            y = carry

        return bin(x)[2:] # removes the first two chars
