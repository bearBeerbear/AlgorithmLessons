/*
Problem Analysis:
We need to compute the prime factorization of n! (n factorial).
For each prime p ¡Ü n, we need to compute the exponent of p in n!.
This is given by Legendre's formula: exponent = floor(n/p) + floor(n/p2) + floor(n/p3) + ...

Solution Approach:
1. Use linear sieve to generate all primes up to n.
2. For each prime p, compute the exponent in n! using Legendre's formula.
3. Output each prime and its corresponding exponent.

Complexity Analysis:
- Prime generation: O(n) using linear sieve.
- Exponent calculation: O(log_p n) for each prime p.
- Total: O(n + ¦Ð(n) * log n) where ¦Ð(n) is number of primes ¡Ü n.

Key Formula:
For prime p, exponent in n! = ¡Æ_{k=1}^{¡Þ} floor(n / p^k)
We stop when p^k > n.
*/

#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>

#define x first
#define y second
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

const int N = 1e6 + 10;
int n;
int primes[N], cnt;
bool st[N];

// Linear sieve to generate all primes up to n
void get_primes(int n) {
    for (int i = 2; i <= n; i++) {
        if (!st[i]) primes[cnt++] = i;
        for (int j = 0; primes[j] <= n / i; j++) {
            st[primes[j] * i] = true;
            if (i % primes[j] == 0) break;
        }
    }
}

void solve() {
    cin >> n;
    
    // Generate all primes ¡Ü n
    get_primes(n);
    
    vector<PII> result;  // Store (prime, exponent) pairs
    
    // For each prime p, compute its exponent in n!
    for (int i = 0; i < cnt; i++) {
        int p = primes[i];
        int exponent = 0;
        int temp = n;
        
        // Legendre's formula: sum of floor(n / p^k)
        while (temp > 0) {
            exponent += temp / p;
            temp /= p;
        }
        
        // Only output primes that appear in n!
        if (exponent > 0) {
            result.push_back({p, exponent});
        }
    }
    
    // Output results
    for (auto item : result) {
        cout << item.x << ' ' << item.y << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int T = 1;
    solve();
    
    return 0;
}
