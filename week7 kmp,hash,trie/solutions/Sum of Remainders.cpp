/*
Problem Analysis:
We need to compute the sum: ¦²_{i=1}^{n} (k mod i)
where k mod i = k - i * floor(k/i).

Rewriting:
sum = ¦²_{i=1}^{n} (k mod i)
    = ¦²_{i=1}^{n} (k - i * floor(k/i))
    = n*k - ¦²_{i=1}^{n} (i * floor(k/i))

We need to efficiently compute ¦²_{i=1}^{n} (i * floor(k/i)).

Solution Approach:
Use number theory block (·Ö¿é³ý·¨) technique:
- For i from 1 to min(n, k), floor(k/i) takes only O(¡Ìk) distinct values.
- Group i values where floor(k/i) is constant.
- For each group [l, r], floor(k/i) is constant = floor(k/l).
- Sum contribution of group: floor(k/l) * ¦²_{i=l}^{r} i = floor(k/l) * (l+r)*(r-l+1)/2

Complexity Analysis:
- Time: O(¡Ìk) using number theory block.
- Space: O(1).

Edge Cases:
- When i > k, k mod i = k (since floor(k/i) = 0).
- When n > k, handle separately: ans += (n-k) * k.
*/

#include <iostream>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>

#define x first
#define y second
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

const int INF = 0x3f3f3f3f, mod = 1e9 + 7, N = 2e5 + 10;
LL n, k;

void solve() {
    cin >> n >> k;
    LL ans = 0;
    
    // Handle case when n > k
    // For i > k, k mod i = k (since k/i < 1, floor(k/i) = 0)
    if (n > k) {
        ans += (n - k) * k;
        n = k;  // Now we only need to handle i ¡Ü k
    }
    
    // For i from 1 to n (where n ¡Ü k), compute k mod i
    // Using number theory block technique
    for (LL l = 1, r; l <= n; l = r + 1) {
        // floor(k/l) is constant in range [l, r]
        LL q = k / l;
        
        // Find right boundary r where floor(k/i) remains constant
        if (q == 0) {
            r = n;  // When q=0, floor(k/i)=0 for all i ¡Ý l
        } else {
            r = min(n, k / q);
        }
        
        // Number of terms in current block
        LL len = r - l + 1;
        
        // Sum of i from l to r: arithmetic series
        LL sum_i = (l + r) * len / 2;
        
        // Add contribution: ¦²_{i=l}^{r} (k mod i) = ¦²_{i=l}^{r} (k - i*q)
        // = k*len - q*sum_i
        ans += k * len - q * sum_i;
    }
    
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int T = 1;
    solve();
    
    return 0;
}
