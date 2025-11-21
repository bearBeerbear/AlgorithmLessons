#include <bits/stdc++.h>

using namespace std;

// Problem: Find minimum total time for people to cross a bridge in groups
// Approach: Dynamic Programming where dp[i] = min time for first i people to cross
// Key idea: For each position i, try grouping last k people (1 ≤ k ≤ m) together
// Time for group = max time in that group
// Transition: dp[i] = min(dp[j] + max(times[j+1..i])) for i-m ≤ j < i

int m, q;
vector<int> times(30);
vector<int> dp(30, INT_MAX); // dp[i] represents minimum time for first i people to cross

int main()
{
    cin >> m >> q;

    // Resize dp array to accommodate q people
    dp.resize(q + 1, INT_MAX);

    // Read crossing times for each person in queue order
    for (int i = 1; i <= q; i++)
    {
        int t;
        cin >> t;
        times[i] = t;
    }

    // Base case: 0 people take 0 time
    dp[0] = 0;

    // Calculate minimum time for each prefix of people
    for (int i = 1; i <= q; i++)
    {
        int cur_max_time = 0;
        // Try grouping last k people together (1 ≤ k ≤ m)
        for (int j = i; j >= max(1, i - m + 1); j--)
        {
            // Update maximum time in current group
            cur_max_time = max(cur_max_time, times[j]);
            // Update dp[i] with minimum time considering this grouping
            dp[i] = min(dp[i], dp[j - 1] + cur_max_time);
        }
    }

    int res = dp[q];
    cout << res;

    return 0;
}