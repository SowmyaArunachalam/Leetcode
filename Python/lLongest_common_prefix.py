'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        new=sorted(strs)
        print(new)
        fst=new[0]
        lst=new[-1]
        s=""
        if(fst == ""):
            return s
        else:
            
            for i in range(0,len(fst)):
                if(fst[i]==lst[i]):
                    s+=fst[i]
                else:
                    return s
        return s