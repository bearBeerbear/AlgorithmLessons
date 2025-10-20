"""
Problem: Given N, find primes A and B such that N = (A + B)/2.
Approach:
1. We have A + B = 2N, so we need two primes summing to 2N.
2. Precompute primes up to 2*10^6 using Sieve of Eratosthenes.
3. For each N, iterate A from 2 upwards, check if A and 2N - A are both primes.
4. Output the first found pair.
"""

import sys


def sieve(limit):
    """Generate a boolean list where is_prime[i] is True if i is prime."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def main():
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    Ns = [int(data[i]) for i in range(1, T + 1)]

    max_N = max(Ns)
    limit = 2 * max_N  # Maximum possible value for A or B
    is_prime = sieve(limit)

    results = []
    for N in Ns:
        target = 2 * N
        # Find primes A and B such that A + B = target
        for A in range(2, target):
            if is_prime[A] and is_prime[target - A]:
                results.append(f"{A} {target - A}")
                break

    print("\n".join(results))


if __name__ == "__main__":
    main()