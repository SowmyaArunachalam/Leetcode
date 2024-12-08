'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
'''

class Solution(object):
    def addDigits(self, num):
        if num<9:
            return num
        
        while(True):
            if(num>=10):
                n1=num//10
                n2=num%10
                num=n1+n2
            else:
                break
        return num