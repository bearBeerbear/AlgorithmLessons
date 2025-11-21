#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 1e3 + 10;
int n, m, f[N][N];
string a, b;

// Problem: Find length of longest common subsequence (LCS) between two strings
// Approach: Dynamic Programming
// State: f[i][j] = length of LCS of first i chars of A and first j chars of B
// Transition:
//   - If a[i] == b[j]: f[i][j] = f[i-1][j-1] + 1
//   - Else: f[i][j] = max(f[i-1][j], f[i][j-1])
// Base case: f[0][j] = 0, f[i][0] = 0
// Result: Maximum value in f[n][j] for all j

void work() {
    // Read input sizes and strings
    cin >> n >> m;
    cin >> a >> b;
    
    // Add dummy character at beginning to make 1-indexed for easier DP implementation
    a = "?" + a, b = "?" + b;
    
    // Fill DP table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // Case 1: Skip current character from string A
            // Case 2: Skip current character from string B
            f[i][j] = max(f[i-1][j], f[i][j-1]);
            
            // Case 3: If current characters match, extend LCS from previous positions
            if (a[i] == b[j]) {
                f[i][j] = max(f[i][j], f[i-1][j-1] + 1);
            }
        }
    }
    
    // Find maximum LCS length in the last row
    // Note: Actually f[n][m] already contains the answer for full strings
    int ans = 0;
    for(int i = 1; i <= m; i++) ans = max(ans, f[n][i]);
    cout << ans << endl;
}

int main() {
    int T = 1;
    while (T--) work();
    return 0;
}