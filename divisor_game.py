class Solution:
    def divisorGame(self, N):
        dp = [False] * (N + 1)
        for i in range(2, N+1):
            for j in range(1, i):
                if i % j == 0:
                    if not dp[i-j]:
                        dp[i] = True
                        break
        return dp[N]


assert Solution().divisorGame(2)
assert not Solution().divisorGame(3)
assert Solution().divisorGame(4)
