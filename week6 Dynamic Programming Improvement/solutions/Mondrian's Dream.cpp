/**
 * Problem: Domino Tiling for N x M Board
 * 
 * Approach:
 * 1. Use state compression DP where each state represents the pattern of filled/unfilled cells
 * 2. Process column by column, considering how dominoes from previous column extend into current column
 * 3. Precompute valid state transitions between adjacent columns
 * 
 * Key Insights:
 * - Represent board state as bitmask: 1 = filled by horizontal domino from previous column, 0 = empty
 * - A valid state must have no consecutive odd-numbered empty cells in any column
 * - Two adjacent columns are compatible if:
 *   a) They don't have overlapping horizontal dominoes (j & k == 0)
 *   b) The combined empty cells form valid vertical domino placements (st[j | k] == true)
 * 
 * DP State:
 * f[i][j] = number of ways to tile first i columns, with state j extending into column i
 * 
 * Time Complexity: O(M * 4^N)
 * Space Complexity: O(M * 2^N)
 */

#include <bits/stdc++.h>
using namespace std;

const int N = 12, M = 1 << N;

long long f[N][M];        // f[col][state]: ways to tile up to column 'col' with state 'state'
bool st[M];               // st[state]: whether state has no odd consecutive zeros
vector<vector<int>> state(M);  // state[j]: list of compatible previous states for current state j

int m, n;

int main() {
    while (cin >> n >> m, n || m) {
        // Part 1: Precompute valid states for a single column
        // A state is valid if it has no odd consecutive zeros (vertical dominoes need pairs)
        for (int i = 0; i < (1 << n); i++) {
            int cnt = 0;        // Count consecutive zeros
            bool isValid = true;
            
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) {
                    // Found a 1, check if previous consecutive zeros count is odd
                    if (cnt & 1) {
                        isValid = false;
                        break;
                    }
                    cnt = 0;    // Reset consecutive zero counter
                } else {
                    cnt++;      // Increment consecutive zero counter
                }
            }
            
            // Check the last segment of consecutive zeros
            if (cnt & 1) isValid = false;
            st[i] = isValid;
        }

        // Part 2: Precompute compatible state transitions between adjacent columns
        for (int j = 0; j < (1 << n); j++) {
            state[j].clear();
            
            for (int k = 0; k < (1 << n); k++) {
                // Check if states j (current) and k (previous) are compatible:
                // 1. No overlapping horizontal dominoes: j & k == 0
                // 2. Combined empty cells form valid vertical placements: st[j | k] == true
                if ((j & k) == 0 && st[j | k]) {
                    state[j].push_back(k);
                }
            }
        }

        // Part 3: Dynamic Programming
        memset(f, 0, sizeof f);
        f[0][0] = 1;  // Base case: empty board with no dominoes extending from previous column
        
        // Process each column from 1 to m
        for (int i = 1; i <= m; i++) {
            for (int j = 0; j < (1 << n); j++) {      // Current column state
                for (auto k : state[j]) {              // Compatible previous column state
                    f[i][j] += f[i - 1][k];
                }
            }
        }

        // Final answer: after processing all m columns, no dominoes extending beyond last column
        cout << f[m][0] << endl;
    }
    
    return 0;
}
