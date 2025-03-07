import math


class Solution:
    def isPrime(self, num: int):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes: list[int] = [num for num in range(left, right + 1) if self.isPrime(num)]

        min_diff = float("inf")
        closest_pair = [-1, -1]
        if len(primes) < 2:
            return closest_pair

        for idx in range(1, len(primes)):
            diff = primes[idx] - primes[idx - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[idx - 1], primes[idx]]
        return closest_pair


sol = Solution()
print(sol.closestPrimes(10, 19))
