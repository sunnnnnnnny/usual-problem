# https://leetcode.cn/problems/valid-parentheses/
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        left_list = ['{','(','[']
        right_list = ['}',')',']']
        if s[0] in right_list:
            return False
        stack = []
        for char in s:
            if char in left_list:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == "}":
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
                if char == ")":
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        return False
                if char == "]":
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        return False
        return len(stack) == 0


obj = Solution()
out = obj.isValid("()")
print(out)
out = obj.isValid("()[]{}")
print(out)
out = obj.isValid("{[]}")
print(out)