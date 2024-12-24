'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
'''
class Solution(object):
    def toLowerCase(self, s):
        s1=""
        for i in s:
            n=ord(i)
            if(n>=65 and n<=90):
                s1+=chr(n+32)
            else:
                s1+=i
        return s1
    