#include <bits/stdc++.h>
using namespace std;

/**
 * Problem: Find the longest duplicate substring in a string
 * 
 * Solution Approach:
 * 1. Use binary search to find the maximum length of duplicate substring
 * 2. For each candidate length, use rolling hash (Rabin-Karp algorithm) to check for duplicates
 * 3. Rolling hash allows efficient substring hash computation in O(1) time
 * 4. Store hashes in unordered_set to detect duplicates
 * 5. Time Complexity: O(n log n) - binary search O(log n) * rolling hash O(n)
 * 6. Space Complexity: O(n) for storing hashes
 */

class Solution {
public:
    int n;
    unsigned long long prime = 31;
    
    string longestDupSubstring(string s) {
        n = s.size();
        int l = 1;          // Minimum possible length of duplicate substring
        int r = n - 1;      // Maximum possible length of duplicate substring
        int pos = -1;       // Starting position of the longest duplicate substring
        int len = 0;        // Length of the longest duplicate substring found

        // Lambda function to check if a duplicate substring of given length exists
        auto find = [&](int len) {
            unsigned long long hash = 0;    // Rolling hash value
            unsigned long long power = 1;   // prime^len for efficient rolling
            
            // Calculate initial hash for first 'len' characters
            for (int i = 0; i < len; i++) {
                hash = hash * prime + (s[i] - 'a');
                power *= prime;
            }
            
            unordered_set<unsigned long long> exist{hash};  // Store seen hashes
            
            // Slide the window and update rolling hash
            for(int i = len; i < n; i++) {
                // Remove leftmost character, add new character
                hash = hash * prime - power * (s[i-len] - 'a') + (s[i] - 'a');
                
                // If hash exists in set, we found a duplicate substring
                if (exist.count(hash)) return (i - len + 1);
                exist.insert(hash);
            }
            return -1;  // No duplicate substring of given length found
        };

        // Binary search for the maximum length of duplicate substring
        while(l <= r) {
            int mid = (l + r) / 2;      // Try middle length
            int start = find(mid);      // Check if duplicate of length 'mid' exists
            
            if (start != -1) {
                // Found duplicate, try longer length
                len = mid;
                pos = start;
                l = mid + 1;
            } else {
                // No duplicate, try shorter length
                r = mid - 1;
            }
        }

        // Return the longest duplicate substring found
        if (pos == -1) return "";
        else return s.substr(pos, len);
    }
};

int main() {
    string s;
    cin >> s;
    Solution t;
    cout << t.longestDupSubstring(s);
    return 0; 
}
