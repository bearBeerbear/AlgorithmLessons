/*
Problem Analysis:
We need to find the closest and most distant consecutive prime numbers within a given interval [L, R].
Constraints: 1 ¡Ü L < R ¡Ü 2^31-1, R-L ¡Ü 10^6.
We need to efficiently find all primes in this large range.

Solution Approach:
1. Precompute primes up to ¡ÌR (max ~50000) using linear sieve.
2. Use segmented sieve to find primes in [L, R]:
   - Mark multiples of precomputed primes in range [L, R].
   - Complexity: O((R-L) log log R).
3. Collect all primes in [L, R] into vector.
4. Find consecutive prime pairs with minimum and maximum differences.

Complexity Analysis:
- Precomputation: O(¡ÌR) using linear sieve.
- Segmented sieve: O((R-L) log log R).
- Total: Efficient for R-L ¡Ü 10^6.

Key Points:
- Use long long to avoid overflow in multiplications.
- Segmented sieve handles large ranges efficiently.
*/

#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>

#define x first
#define y second
#define int long long
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

const int INF = 0x3f3f3f3f;
const int N = 1e6 + 10;
const int MAX_PRE = 1050000;  // ¡Ì(2^31) ¡Ö 46340, use 1050000 for safety

int l, r;
bool st[MAX_PRE + 50000];      // For precomputation sieve
int primes[MAX_PRE + 50000], cnt;

// Linear sieve to find primes up to n
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
    // Precompute primes up to ¡ÌR_max
    get_primes(1050000);
    
    while (cin >> l >> r) {
        vector<int> v;  // Store primes in [l, r]
        
        // Case 1: Range fits in precomputed primes
        if (r <= 1050000) {
            for (int i = 0; i < cnt; i++) {
                if (primes[i] >= l && primes[i] <= r) {
                    v.push_back(primes[i]);
                }
            }
        }
        // Case 2: Larger range, use segmented sieve
        else {
            // Reuse st array for segmented sieve (offset by l)
            memset(st, 0, sizeof(st));
            
            // Mark multiples of precomputed primes in [l, r]
            for (int i = 0; i < cnt; i++) {
                int p = primes[i];
                // Start from first multiple of p >= l
                LL start = max(p * 2LL, (l + p - 1) / p * p);
                
                // Mark multiples of p in [l, r]
                for (LL j = start; j <= r; j += p) {
                    st[j - l] = true;  // Offset by l
                }
            }
            
            // Collect primes from marked array
            for (int i = 0; i <= r - l; i++) {
                if (!st[i] && i + l >= 2) {  // Ensure number ¡Ý 2
                    v.push_back(i + l);
                }
            }
        }
        
        // Find closest and most distant consecutive primes
        int min_dist = INF, max_dist = -INF;
        PII closest_pair = {-1, -1}, distant_pair = {-1, -1};
        
        for (int i = 1; i < v.size(); i++) {
            int dist = v[i] - v[i - 1];
            
            if (dist < min_dist) {
                min_dist = dist;
                closest_pair = {v[i - 1], v[i]};
            }
            
            if (dist > max_dist) {
                max_dist = dist;
                distant_pair = {v[i - 1], v[i]};
            }
        }
        
        // Output results
        if (closest_pair.x != -1) {
            printf("%lld,%lld are closest, %lld,%lld are most distant.\n", 
                   closest_pair.x, closest_pair.y, distant_pair.x, distant_pair.y);
        } else {
            printf("There are no adjacent primes.\n");
        }
    }
}

signed main() {
    int T = 1;
    solve();
    return 0;
}
