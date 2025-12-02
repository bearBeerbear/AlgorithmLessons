/*
Problem Analysis:
We need to check if a binary string contains 7 consecutive 0's or 7 consecutive 1's.
This indicates a "dangerous" situation in the football match context.

Solution Approach:
1. If string length is less than 7, output "NO" immediately.
2. Scan the string with a sliding window of length 7.
3. Check each substring of length 7:
   - If it equals "0000000" or "1111111", output "YES".
4. If no dangerous substring found, output "NO".

Complexity Analysis:
- Time: O(n) where n is string length.
- Space: O(1) excluding input storage.
*/

#include <bits/stdc++.h>
using namespace std;

string a;

int main() {
    // Read input string
    cin >> a;
    
    // If string is too short, cannot have 7 consecutive characters
    if (a.size() < 7) {
        cout << "NO";
        return 0;
    }
    
    // Check all possible substrings of length 7
    for (int i = 0; i <= a.size() - 7; i++) {
        // Extract substring of length 7 starting at position i
        string substring = a.substr(i, 7);
        
        // Check if substring is all 0's or all 1's
        if (substring == "0000000" || substring == "1111111") {
            cout << "YES";
            return 0;
        }
    }
    
    // No dangerous substring found
    cout << "NO";
    return 0;
}
