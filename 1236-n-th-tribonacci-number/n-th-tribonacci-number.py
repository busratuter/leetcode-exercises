class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        tribonacci = [0] * (n + 1)
        tribonacci[0] = 0
        tribonacci[1] = 1
        tribonacci[2] = 1

        for i in range(3, n + 1):
            tribonacci[i] = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]

        return tribonacci[n]
