class Solution:
    def longestValidParentheses(self, s):
        stack = []
        dp = [0] * len(s)
        for idx, ele in enumerate(s):
            if ele == '(':
                stack.append(idx)
            else:
                if stack:
                    left_position = stack.pop()
                    dp[idx] = dp[left_position-1] + idx - left_position + 1
        return max(dp)


assert Solution().longestValidParentheses('(()') == 2
assert Solution().longestValidParentheses('()()') == 4
assert Solution().longestValidParentheses(')()())') == 4


