#include <bits/stdc++.h>
using namespace std;

/**
 * Problem: Check if two strings are anagrams of each other
 * 
 * Solution Approach:
 * 1. Anagrams must have the same length and same character frequency
 * 2. Use a hash map to count character frequencies in first string
 * 3. Decrement counts using characters from second string
 * 4. If all counts become zero, strings are anagrams
 * 5. Time Complexity: O(n) where n is string length
 * 6. Space Complexity: O(1) since fixed number of characters (26 for lowercase)
 */

class Solution {
public:
    bool isAnagram(string s, string t) {
        // Check if strings have same length (prerequisite for anagrams)
        if (s.length() != t.length())
            return false;
        
        // Create frequency dictionary for characters
        unordered_map<char, int> dic;
        
        // Count frequency of each character in string s
        for (char c : s) {
            dic[c] += 1;
        }
        
        // Decrement frequency for each character in string t
        for (char c : t) {
            dic[c] -= 1;
        }
        
        // Check if all character frequencies are zero
        for (auto kv : dic) {
            if (kv.second != 0)
                return false;
        }
        
        return true;
    }
};

int main() {
    string s, t;
    cin >> s >> t;
    Solution w;
    cout << (w.isAnagram(s, t) ? "true" : "false");
    return 0; 
}
