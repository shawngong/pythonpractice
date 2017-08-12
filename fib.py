class Solution(object):
    def fib(self, i, memo = None):
        if memo == None:
            return self.fib(i, [0] * (i + 1))
        if i == 0 or i == 1:
            return i
        if (memo[i] == 0):
            memo[i] = self.fib(i - 1, memo) + self.fib(i - 2, memo)
        return memo[i]

if __name__ == '__main__':
    print Solution().fib(10)
