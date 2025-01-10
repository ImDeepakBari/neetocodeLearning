"""
Given two strings S and T , return true if T is anagram of S , and false otherwise.

Example:

    Input : s = "anagram" , t = "nagaram"
    Output : true


Example 2 :
    Input : s = "rat" , t = "car"
    Output : false

"""


class Solution:

    def valid_anagram(self, s, t):

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countT:
            if countT[c] != countS.get(c, 0):
                return False

        return True


answer = Solution()

sol1 = answer.valid_anagram('anagram', 'gramana')
print(sol1)

sol2 = answer.valid_anagram('caracer', 'carrace')
print(sol2)

sol3 = answer.valid_anagram('pandahouse', 'housebear')
print(sol3)
