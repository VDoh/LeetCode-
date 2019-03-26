class Solution:
    def is32(number: int) -> bool:
        if(number < (-2**31) or number > (2**31 -1 )):
            return True
        else :
            return False 

    def reverse(self, x: int) -> int:
        solution = str(x)
        copy = ""
        j = len(solution)-1
        myrange = len(solution)
        char = "-"

        if solution[0] is "-":
            copy+=str(char)
            myrange -=1

        for i in range(myrange):
            copy+=solution[j]
            j -=1

        copy = int(copy)
        AmI = Solution.is32(copy)
        if AmI is True:
            return 0
        else: 
            return copy

o = Solution()
reversed: int = o.reverse(-321)

print(reversed)

