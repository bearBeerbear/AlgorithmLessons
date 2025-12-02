/*
Problem Analysis:
We need to count the number of passwords of length N that:
1. Contain only lowercase English letters
2. Do NOT contain substring T
We need to compute the result modulo 1e9+7.

Solution Approach:
This is a string DP problem using KMP automaton:
1. Precompute KMP next array for pattern T.
2. Use DP: f[i][j] = number of strings of length i where the longest suffix matching T is j characters.
3. For each state f[i][j], try adding all 26 letters:
   - Find the new state k using KMP transition from j with character ch
   - If k == m (full match of T), skip this transition (invalid password)
   - Otherwise, add f[i][j] to f[i+1][k]
4. Answer is sum of f[N][j] for all j < m.

Complexity Analysis:
- Time: O(26 * N * M) where N is password length, M is pattern length.
- Space: O(N * M) for DP table.
*/

#include <iostream>
#include <cstring>

using namespace std;

const int N = 55;
const int MOD = 1e9 + 7;

int n, m;
char s[N];
int f[N][N], ne[N];

int main() {
    // Read password length n and pattern string s
    // Using scanf instead of cin for reading pattern string with offset
    scanf("%d%s", &n, s + 1);
    
    m = strlen(s + 1);
    
    // Precompute KMP next array for pattern T
    for (int i = 2, j = 0; i <= m; ++i) {
        while (j && s[i] != s[j + 1]) j = ne[j];
        if (s[i] == s[j + 1]) ++j;
        ne[i] = j;
    }
    
    // Initialize DP: empty string has 1 way with 0 matched characters
    f[0][0] = 1;
    
    // DP transition: build password character by character
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            // Try adding each possible character
            for (char ch = 'a'; ch <= 'z'; ++ch) {
                int ptr = j;    // Current state pointer
                
                // Find next state using KMP transition
                while (ptr && s[ptr + 1] != ch) ptr = ne[ptr];
                if (s[ptr + 1] == ch) ++ptr;
                
                // If ptr < m (no full pattern match), add to DP
                f[i + 1][ptr] = (f[i + 1][ptr] + f[i][j]) % MOD;
            }
        }
    }
    
    // Sum all valid states of length n
    int res = 0;
    for (int j = 0; j < m; ++j) res = (res + f[n][j]) % MOD;
    
    cout << res << endl;
    return 0;
}
