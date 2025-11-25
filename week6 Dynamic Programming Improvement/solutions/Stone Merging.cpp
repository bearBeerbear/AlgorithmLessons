/**
 * Problem: Minimum Cost to Merge Stones
 * 
 * Approach:
 * 1. We use interval dynamic programming to solve this problem
 * 2. Precompute prefix sums to quickly calculate the sum of any subarray
 * 3. f[i][j] represents the minimum cost to merge stones from pile i to pile j
 * 4. We iterate over all possible lengths of intervals, then all starting positions,
 *    and finally all possible split points within each interval
 * 
 * Key Insight:
 * - The cost of merging interval [i,j] equals the cost of merging [i,k] plus 
 *   the cost of merging [k+1,j] plus the total weight of stones from i to j
 * - We need to try all possible split points k to find the optimal merging order
 * 
 * Recurrence Relation:
 * f[i][j] = min(f[i][k] + f[k+1][j] + s[j] - s[i-1]) for all k in [i, j-1]
 * 
 * Time Complexity: O(N^3)
 * Space Complexity: O(N^2)
 */

#include <iostream>
#include <cstring>

using namespace std;

const int N = 307;

int a[N], s[N];  // a: stone weights, s: prefix sums
int f[N][N];     // f[i][j]: min cost to merge stones from i to j

int main() {
    int n;
    cin >> n;

    // Read input and compute prefix sums
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        s[i] = s[i - 1] + a[i];  // s[i] = sum of first i stones
    }

    // Initialize DP table with large values
    memset(f, 0x3f, sizeof f);
    
    // Interval DP: iterate by interval length
    for (int len = 1; len <= n; len++) {
        for (int i = 1; i + len - 1 <= n; i++) {
            int j = i + len - 1;  // Calculate right endpoint
            
            // Base case: single pile requires no merging
            if (len == 1) {
                f[i][j] = 0;
                continue;
            }

            // Try all possible split points
            for (int k = i; k <= j - 1; k++) {
                // Update minimum cost: merge [i,k] and [k+1,j], then add total weight
                f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + s[j] - s[i - 1]);
            }
        }
    }

    // Output minimum cost to merge all stones from pile 1 to n
    cout << f[1][n] << endl;

    return 0;
}
