#include <bits/stdc++.h>
using namespace std;

/**
 * Problem: Find the length of the longest substring without repeating characters
 * 
 * Solution Approach:
 * 1. Use sliding window technique with two pointers i and j
 * 2. Use a vector to store the last occurrence index of each character
 * 3. Expand the window by moving j forward
 * 4. When a duplicate is found, move i to the position after the last occurrence
 * 5. Update the maximum length at each step
 * 
 * Time Complexity: O(n) - single pass through the string
 * Space Complexity: O(1) - fixed size vector for ASCII characters
 */

int lengthOfLongestSubstring(string s) {
    // Store the last occurrence index of each character
    // Initialize with 0 (meaning character hasn't appeared yet)
    vector<int> m(128, 0);
    int ans = 0;    // Maximum length found so far
    int i = 0;      // Left pointer of the sliding window
    
    for (int j = 0; j < s.size(); j++) {
        // Move i to the position after the last occurrence of current character
        // This ensures no duplicates in current window [i, j]
        i = max(i, m[s[j]]);
        
        // Update the last occurrence of current character to position j+1
        // We store j+1 so that when we see this character again, 
        // we can move i to j+1 to skip the duplicate
        m[s[j]] = j + 1;
        
        // Update maximum length if current window is larger
        ans = max(ans, j - i + 1);
    }
    return ans;
}

int main() {
    string s;
    cin >> s;
    cout << lengthOfLongestSubstring(s);
    return 0; 
}
