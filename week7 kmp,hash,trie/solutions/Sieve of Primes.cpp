/*
Problem Analysis:
We need to count the number of prime numbers less than or equal to n.
This requires an efficient algorithm for prime counting since n can be up to 1e6.

Solution Approach:
Use the linear sieve (Euler's sieve) algorithm:
1. Maintain an array primes[] to store found primes.
2. Maintain a boolean array st[] to mark composite numbers.
3. For each number i from 2 to n:
   - If i is not marked (st[i] is false), it's prime, add to primes[].
   - For each prime p in primes[]:
     * Mark i * p as composite.
     * If i is divisible by p, break (maintain linear complexity).

Key Properties:
- Each composite number is marked exactly once by its smallest prime factor.
- Time complexity: O(n)
- Space complexity: O(n)

Complexity Analysis:
- Time: O(n) - each number is processed once.
- Space: O(n) for boolean array and primes array.
*/

#include <iostream>
#include <utility>
#include <vector>
using namespace std;

const int N = 1e6 + 10;  // Maximum n value

int n;
int primes[N];           // Store prime numbers
bool st[N];              // st[i] = true if i is composite (not prime)

// Linear sieve to count primes up to n
int get_prime(int n) {
    int res = 0;  // Count of primes found
    
    for (int i = 2; i <= n; i++) {
        // If i is not marked as composite, it's prime
        if (!st[i]) {
            primes[res++] = i;  // Add to primes list
        }
        
        // Mark multiples of primes as composite
        for (int j = 0; primes[j] <= n / i; j++) {
            st[primes[j] * i] = true;  // Mark i * primes[j] as composite
            
            // This ensures each composite is marked by its smallest prime factor
            if (i % primes[j] == 0) {
                break;
            }
        }
    }
    
    return res;  // Return count of primes
}

int main() {
    cin >> n;
    cout << get_prime(n);
    return 0;
}
