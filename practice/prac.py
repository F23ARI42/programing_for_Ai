class Solution(object):
    def addBinary(self, a, b):
        add=int(a,2)+int(b,2)
        return bin(add)[2:]
sol=Solution()
print(sol.addBinary("11","1"))
