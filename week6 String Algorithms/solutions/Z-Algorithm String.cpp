#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int N = 1000010;
char p[N], s[N]; // p is pattern string, s is text string

/**
 * Problem: String pattern matching using Z-algorithm
 * 
 * Solution Approach:
 * 1. Z-algorithm computes Z-array where Z[i] is the length of longest substring 
 *    starting at i that matches the prefix of the string
 * 2. Create new string: pattern + '$' + text
 * 3. Compute Z-array for this combined string
 * 4. Where Z[i] == pattern length, we found a match at position i
 * 5. Time Complexity: O(n + m) linear time
 * 6. Space Complexity: O(n + m) for Z-array
 */

// Function to compute Z-array for a given string
vector<int> computeZArray(const string& str) {
    int n = str.length();
    vector<int> z(n, 0);
    int l = 0, r = 0; // [l, r] represents the current Z-box
    
    for (int i = 1; i < n; i++) {
        if (i <= r) {
            // We are inside the Z-box, can use previously computed values
            z[i] = min(r - i + 1, z[i - l]);
        }
        
        // Explicitly check for characters beyond the Z-box
        while (i + z[i] < n && str[z[i]] == str[i + z[i]]) {
            z[i]++;
        }
        
        // Update Z-box if we found a longer one
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    
    return z;
}

int main()
{
    int n, m; // n is pattern length, m is text length
    cin >> n >> p >> m >> s;
    
    // Create combined string: pattern + '$' + text
    string combined = string(p, n) + "$" + string(s, m);
    
    // Compute Z-array for combined string
    vector<int> z = computeZArray(combined);
    
    // Pattern length
    int patternLen = n;
    
    // Search for pattern occurrences in text
    // Text starts after pattern + '$', so at index patternLen + 1
    for (int i = patternLen + 1; i < (int)combined.length(); i++) {
        // If Z-value equals pattern length, we found a match
        if (z[i] == patternLen) {
            // Calculate starting position in original text
            // i - (patternLen + 1) gives position in text
            cout << i - (patternLen + 1) << ' ';
        }
    }
    
    return 0;
}
