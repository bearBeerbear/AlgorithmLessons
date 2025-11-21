#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 5010;

// Problem: Find minimum asymmetry value for all possible mountain range lengths
// Approach: Dynamic Programming where dp[i][j] = asymmetry of range starting at i with length j
// Key idea: For a range [l, r], asymmetry is sum of |h[l+i] - h[r-i]| for all symmetric pairs
// We can compute this recursively: dp[i][j] = dp[i+1][j-2] + |h[i] - h[i+j-1]|
// Base case: ranges of length 1 have asymmetry 0, ranges of length 2 have |h[i] - h[i+1]|

int h[N], ans[N];
int dp[N][N];   // dp[i][j] represents asymmetry of mountain range starting at i with length j

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) scanf("%d", &h[i]);
    
    // Initialize answers with large values
    memset(ans, 0x3f, sizeof ans);
    ans[1] = 0;  // Single mountain has asymmetry 0
    
    // Calculate asymmetry for all possible ranges
    for (int k = 1; k < n; ++k) {  // k represents current length - 1
        for (int i = 1; i <= n - k; ++i) {  // i is starting position
            // Current range: [i, i+k] with length k+1
            // Asymmetry = asymmetry of inner range [i+1, i+k-1] + |h[i] - h[i+k]|
            dp[i][k + 1] = dp[i + 1][k - 1] + abs(h[i] - h[i + k]);
            // Update minimum asymmetry for current length
            ans[k + 1] = min(ans[k + 1], dp[i][k + 1]);
        }
    }
    
    // Output results for all lengths from 1 to n
    for (int i = 1; i <= n; i++) cout << ans[i] << " ";
    return 0;
}