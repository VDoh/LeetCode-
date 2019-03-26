class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        lengthOfA: int = len(A)
        lengthOfB: int = len(B)
        compareString = ""
        temp=""
    
        if(lengthOfA is lengthOfB and lengthOfA > 0):
            if(A == B):
                occurance = set()
                for i in A:
                    if(i in occurance):
                        return True
                    occurance.add(i)
                return False 
            else: 
                for i in range(lengthOfA):
                    if(A[i] != B[i]):
                        index = set()
                        index.add(i)
                        temp = A[i] + A[i-1] 
                        compareString = A[0:i-1] + temp
                if A[index[0]] == B[index[1]] and  A[index[1]] == B[index[0]]:
                    return True
                if compareString == "":
                    return True
                if compareString == B:
                    return True
                else:
                    return False
        else:
            return False 
o = Solution()
o.buddyStrings("ab","ab")
