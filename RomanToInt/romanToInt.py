class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value: int=0
        flag: bool=False
        iterator = 0
        
        for i in range(len(s)):
            try:
                if dictionary[s[iterator+1]] > dictionary[s[iterator]]:
                    value = value + (dictionary[s[iterator+1]]-dictionary[s[iterator]])
                    flag=True
                    iterator=iterator+1
                else:
                    value  = value + dictionary[s[iterator]]
                    flag=False
            except IndexError:
                if flag == False:
                    value  = value + dictionary[s[iterator]]
                break
            iterator = iterator + 1
        return value