/*
Problem Analysis:
We need to find the number ¡Ü n that has the maximum number of divisors.
If multiple numbers have the same maximum divisor count, choose the smallest one.

Solution Approach:
Use DFS with pruning to search through all "highly composite numbers":
1. Highly composite numbers have prime factorization of the form: p1^e1 * p2^e2 * ... * pk^ek
   where p1 < p2 < ... < pk are consecutive primes and e1 ¡Ý e2 ¡Ý ... ¡Ý ek ¡Ý 1.
2. Number of divisors = (e1+1)*(e2+1)*...*(ek+1).
3. Use DFS to try all valid exponent combinations:
   - Primes are in increasing order: 2, 3, 5, 7, 11, ...
   - Exponents are non-increasing: e_i ¡Ý e_{i+1}.
4. Prune when current product exceeds n.

Complexity Analysis:
- The search space is limited since exponents decrease rapidly.
- Practically runs very fast for n ¡Ü 2*10^9.

Key Observations:
- Use long long to avoid overflow.
- Start with largest possible exponents and decrease.
- Track maximum divisor count and smallest number with that count.
*/

#include <iostream>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <climits>

#define x first
#define y second
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

const int INF = 0x3f3f3f3f, mod = 1e9 + 7, N = 2e5 + 10;

int n;
// First few primes (enough for n ¡Ü 2*10^9)
int primes[10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 31};

LL max_num;      // Current number with maximum divisors
LL max_divisors; // Maximum divisor count found so far

// DFS to search for number with maximum divisors ¡Ü n
// u: current prime index in primes[]
// num: current number product
// divisors: current divisor count = ¡Ç(e_i + 1)
// last_exp: exponent of previous prime (ensures e_i ¡Ý e_{i+1})
void dfs(int u, LL num, LL divisors, int last_exp) {
    // Update maximum if current has more divisors,
    // or same divisors but smaller number
    if (divisors > max_divisors || (divisors == max_divisors && num < max_num)) {
        max_divisors = divisors;
        max_num = num;
    }
    
    // If no more primes, return
    if (u >= 10) return;
    
    // Try different exponents for current prime
    // Exponent starts from 1 up to last_exp (non-increasing constraint)
    for (int exp = 1; exp <= last_exp; exp++) {
        // Check if multiplying by prime^exp would exceed n
        if (num > n / primes[u]) break;  // Avoid overflow
        
        // Multiply by prime^exp
        num *= primes[u];
        
        // Recursively try next prime with reduced exponent constraint
        dfs(u + 1, num, divisors * (exp + 1), exp);
    }
}

void solve() {
    cin >> n;
    
    // Initialize
    max_num = 1;
    max_divisors = 1;
    
    // Start DFS with first prime (2), initial number 1, 
    // divisor count 1, and large initial exponent (log2(n) ¡Ü 31)
    dfs(0, 1, 1, 31);
    
    cout << max_num << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int T = 1;
    solve();
    
    return 0;
}
