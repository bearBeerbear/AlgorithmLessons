/**
 * Problem: Bounded Knapsack with Monotonic Queue Optimization
 * 
 * Approach:
 * 1. We use dynamic programming with a sliding window maximum technique
 * 2. For each item type, we process the knapsack capacity in modulo classes based on item volume
 * 3. For each residue class r (0 <= r < v[i]), we maintain a monotonic queue that stores indices
 *    of states in decreasing order of their value contribution
 * 4. The queue helps us efficiently find the maximum value for the current state while respecting
 *    the quantity constraint s[i]
 * 
 * Key Insight:
 * - Instead of iterating through all possible quantities of each item, we notice that for a given
 *   remainder r modulo v[i], the states form an arithmetic progression
 * - We can use a deque to maintain a sliding window maximum over these states
 * - The window size is determined by the maximum quantity s[i] of the current item type
 * 
 * Time Complexity: O(N * V)
 * Space Complexity: O(V)
 */

#include <iostream>
#include <cstring>

using namespace std;

const int N = 1010, M = 20010;

int n, m;
int v[N], w[N], s[N];  // volume, value, and quantity limits for each item type
int f[M], g[M];        // f: current DP state, g: previous DP state (for rolling array)
int q[M];              // monotonic queue storing indices

int main()
{
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) 
        cin >> v[i] >> w[i] >> s[i];
    
    // Process each item type
    for (int i = 1; i <= n; ++i)
    {
        // Save the previous state
        memcpy(g, f, sizeof g);
        
        // Process each residue class modulo v[i]
        for (int r = 0; r < v[i]; ++r)
        {
            int hh = 0, tt = -1;  // head and tail of the deque
            
            // Process all states in this residue class
            for (int j = r; j <= m; j += v[i])
            {
                // Remove indices that are too far away (exceed quantity limit)
                while (hh <= tt && j - q[hh] > s[i] * v[i]) 
                    hh++;
                
                // Maintain monotonic decreasing order in the deque
                // Remove indices that cannot contribute more value than current state
                while (hh <= tt && g[q[tt]] + (j - q[tt]) / v[i] * w[i] <= g[j]) 
                    tt--;
                
                // Add current index to the deque
                q[++tt] = j;
                
                // Update current state using the best value from the deque
                f[j] = g[q[hh]] + (j - q[hh]) / v[i] * w[i];
            }
        }
    }
    
    cout << f[m] << endl;
    return 0;
}
