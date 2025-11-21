#include<bits/stdc++.h>
using namespace std;

// Problem: Maximum score from knocking down bowling pins in k shots of width w
// Approach: Dynamic Programming where dp[i][j] = max score using first i pins with j shots
// Key idea: For each position i, we can either skip pin i or take a shot ending at i
// If we take a shot ending at i, it covers pins [i-w+1, i] with score = sum[i] - sum[i-w]
// Transition: dp[i][j] = max(dp[i-1][j], dp[i-w][j-1] + (sum[i]-sum[i-w]))
// Base case: dp[0][j] = 0 for all j

void solve()
{
    int n, k, w;
    cin >> n >> k >> w;
    vector<int> a(n + 1);
    vector<int> sum(n + 1, 0);
    
    // Read pin scores and compute prefix sums
    for(int i = 1; i <= n; i++) cin >> a[i];
    for(int i = 1; i <= n; i++) sum[i] = sum[i - 1] + a[i];
    
    // DP table: dp[i][j] = max score with first i pins and j shots
    vector<vector<int>> dp(n + 1, vector<int>(min(n, k) + 1, 0));
    
    // Fill DP table
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= min(n, k); j++) {
            // Option 1: Don't use pin i in current shot
            dp[i][j] = dp[i - 1][j];
            // Option 2: Use a shot ending at pin i (covers [i-w+1, i])
            if(i - w >= 0) {
                dp[i][j] = max(dp[i][j], dp[i - w][j - 1] + sum[i] - sum[i - w]);
            } else {
                // Handle case where shot covers from beginning
                dp[i][j] = max(dp[i][j], dp[0][j - 1] + sum[i] - sum[0]);
            }
        }
    }
    cout << dp[n][k] << endl;
}

signed main()
{
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
    return 0;
}