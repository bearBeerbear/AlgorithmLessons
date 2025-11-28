#include <iostream>

using namespace std;

const int N = 1000010;
char p[N], s[N]; // p is pattern string, s is text string to search in
int ne[N];       // next array for KMP algorithm
int n, m;        // n is pattern length, m is text length

/**
 * Problem: String pattern matching using KMP algorithm
 * 
 * Solution Approach:
 * 1. Preprocess pattern string to compute "next" array
 *    - next[i] stores the length of longest proper prefix which is also suffix for p[0...i]
 * 2. Use next array to avoid redundant comparisons during matching
 * 3. When mismatch occurs, use next array to determine new starting position in pattern
 * 4. Time Complexity: O(n + m) for preprocessing and matching
 * 5. Space Complexity: O(n) for next array
 */

int main()
{
    cin >> n >> p >> m >> s;

    // Build next array for pattern string
    ne[0] = -1; // No proper prefix for single character

    // Compute next array using dynamic programming approach
    for (int i = 1, j = -1; i < n; i ++)
    {
        // When mismatch occurs, backtrack using next array
        while (j != -1 && p[i] != p[j + 1])
        {
            j = ne[j]; // Move j to previous longest prefix-suffix position
        }
        
        // If characters match, extend the prefix-suffix length
        if (p[i] == p[j + 1]) 
        {
            j ++; // Increase matched prefix length
        }
        
        ne[i] = j; // Store the longest prefix-suffix ending at position i
    }

    // KMP pattern matching
    for (int i = 0, j = -1; i < m; i ++)
    {
       // When mismatch occurs, use next array to skip unnecessary comparisons
       while (j != -1 && s[i] != p[j + 1])
       {
           j = ne[j]; // Fall back to previous matching position
       }
       
       // If characters match, move to next character in pattern
       if (s[i] == p[j + 1])
       {
           j ++; // Advance pattern pointer
       }
       
       // Complete pattern matched
       if (j == n - 1) 
       {
           // Output starting index of match (0-based indexing)
           cout << i - j << ' ';

           // Continue searching for next occurrence
           // Use next array to find next possible match position
           j = ne[j]; 
       }
    }

   return 0;
}
