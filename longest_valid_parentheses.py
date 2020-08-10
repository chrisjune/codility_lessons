class Solution:
    def longestValidParentheses(self, s):
        stack = []
        dp = [0] * len(s)
        for idx, ele in enumerate(s):
            if ele == '(':
                stack.append(idx)
                queue = []
                count = 0
                inner = False
                for ele in s:
                    queue.append(ele)
                    if ''.join(queue[-2:]) == "()":
                        count += 2
                return count
            else:
                if stack:
                    left_position = stack.pop()
                    dp[idx] = dp[left_position-1] + idx - left_position + 1
        return max(dp)


assert Solution().longestValidParentheses('(()') == 2
assert Solution().longestValidParentheses('()()') == 4
assert Solution().longestValidParentheses(')()())') == 4


