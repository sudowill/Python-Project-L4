import string

class Solution:
    def solve(self, s, k):
        def shift(c):
            i = ord(c) - ord('a')
            i += k
            i %= 26
            return chr(ord('a') + i)

        return "".join(map(shift, s))
        
ob = Solution()
print(ob.solve("abcd", 20))


    if the in solve:
        print("Found shift")
        print("Processing  shift")