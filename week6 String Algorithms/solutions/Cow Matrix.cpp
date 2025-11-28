#include <bits/stdc++.h>
using namespace std;

/**
 * Problem: Find the smallest repeating unit in a 2D pattern
 * 
 * Solution Approach:
 * 1. First find the smallest repeating height (k) by building KMP next array for rows
 * 2. Extract the first k rows and transpose to work on columns
 * 3. Find the smallest repeating width by building KMP next array for transposed columns
 * 4. The answer is the product of smallest repeating height and width
 * 
 * Steps:
 * - Use KMP algorithm to find period in row direction
 * - Transpose the minimal row pattern to work on columns
 * - Use KMP again to find period in column direction
 * - Multiply both periods to get total minimal repeating unit area
 */

string s[10005], _s[10005]; // s: original grid, _s: transposed grid
int nxt[10005];            // KMP next array

int main()
{
    int n, m; // n: number of rows, m: number of columns
    cin >> n >> m;
    
    // Read the grid
    for (int i = 0; i < n; i++) 
        cin >> s[i];
    
    // Step 1: Find smallest repeating height using KMP on rows
    nxt[0] = -1; // Initialize KMP next array
    for (int i = 1; i <= n; i++) {
        int j = nxt[i - 1];
        // KMP backtracking to find longest prefix-suffix
        while (j >= 0 && s[i - 1] != s[j]) 
            j = nxt[j];
        nxt[i] = j + 1;
    }
    
    // Calculate minimal repeating height (period in row direction)
    int k = n - nxt[n];
    
    // Step 2: Transpose the minimal pattern (first k rows)
    for (int i = 0; i < m; i++)
        for (int j = 0; j < k; j++)
            _s[i] += s[j][i]; // Build transposed grid
    
    // Copy transposed grid back to s for KMP processing
    for (int i = 0; i < m; i++) 
        s[i] = _s[i];
    
    // Step 3: Find smallest repeating width using KMP on transposed columns
    nxt[0] = -1; // Reset KMP next array
    for (int i = 1; i <= m; i++) {
        int j = nxt[i - 1];
        // KMP backtracking for column direction
        while (j >= 0 && s[i - 1] != s[j]) 
            j = nxt[j];
        nxt[i] = j + 1;
    }
    
    // Calculate minimal repeating width (period in column direction)
    int width_period = m - nxt[m];
    
    // Final answer: area of smallest repeating unit
    int ans = width_period * k;
    cout << ans << endl;
    
    return 0;
}
