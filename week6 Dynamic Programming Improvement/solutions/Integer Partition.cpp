/**
 * Problem: Integer Partition Count
 * 
 * Approach:
 * 1. We use dynamic programming to count the number of ways to partition integer n
 * 2. This solution uses an "unbounded knapsack" approach where:
 *    - The target sum is n
 *    - Available items are integers 1, 2, ..., n (each can be used multiple times)
 *    - The order doesn't matter (automatically ensured by processing items in order)
 * 
 * 3. DP State: f[i][j] = number of ways to represent j using integers from 1 to i
 * 
 * Key Insight:
 * - We can either not use integer i: f[i][j] = f[i-1][j]
 * - Or use integer i at least once: f[i][j] += f[i][j-i]
 * - This ensures partitions are in non-increasing order (avoiding duplicates)
 * 
 * Recurrence Relation:
 * f[i][j] = f[i-1][j] + f[i][j-i]  (when j >= i)
 * f[i][j] = f[i-1][j]              (when j < i)
 * 
 * Base Case: f[i][0] = 1 for all i (empty partition)
 * 
 * Time Complexity: O(N^2)
 * Space Complexity: O(N^2)
 */

#include <iostream>

using namespace std;

const int N = 1e3 + 7, mod = 1e9 + 7;

int f[N][N];  // f[i][j]: number of partitions of j using numbers 1..i

int main() {
    int n;
    cin >> n;

    // Initialize base cases
    for (int i = 0; i <= n; i++) {
        f[i][0] = 1;  // There's exactly 1 way to partition 0: the empty partition
    }

    // Fill DP table
    for (int i = 1; i <= n; i++) {      // i: current maximum number we can use
        for (int j = 0; j <= n; j++) {  // j: target sum we want to partition
            // Option 1: Don't use number i at all
            f[i][j] = f[i - 1][j] % mod;
            
            // Option 2: Use number i at least once (if we have enough capacity)
            if (j >= i) {
                f[i][j] = (f[i - 1][j] + f[i][j - i]) % mod;
            }
        }
    }

    cout << f[n][n] << endl;  // Answer: partitions of n using numbers 1..n

    return 0;
}
