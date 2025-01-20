"""
Wap to reverse a string.

Example 1:

    Input : "Hello this is my Mac Book"
    Output : "Book Mac my is this Hello"

"""


class Solution:

    def reverse_string(self, input_str):
        output = input_str.split()
        print(output)

        i = len(output) - 1
        rev_output = []
        while i >= 0:
            rev_output.append(output[i])
            i -= 1

        print(" ".join(rev_output))


anser = Solution()
sol = anser.reverse_string("Hello my name is Deepak Bari")
print(sol)

"""
Example: 

    Input: "Hello this is MacBook pro"
    Output: "olleH siht si kooBcaB orp"
    
"""


class Reverse:

    def reverse_content(self, str1):
        temp = str1.split()
        print(temp)
        output = []
        for i in temp:
            output.append(i[::-1])

        print(" ".join(output))


sol = Reverse()
sol.reverse_content(str1="The balck Brown fox run over the lazy dog")

"""
Example 1:
    Input : 
"""