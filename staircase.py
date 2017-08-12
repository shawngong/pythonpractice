import math

class Solution(object):
    def staircase(self, n):
        memo = [-1] * (n + 1)
        return self.staircase_helper(n, memo)
    def staircase_helper(self, n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n] != -1:
            return memo[n]
        else:
            memo[n] = self.staircase_helper(n - 1, memo) + self.staircase_helper(n - 2, memo) + self.staircase_helper(n - 3, memo)
            return memo[n]

if __name__ == '__main__':
    print Solution().staircase(3);
