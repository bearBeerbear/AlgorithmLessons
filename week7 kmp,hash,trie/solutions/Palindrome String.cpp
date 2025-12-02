/*
Problem Analysis:
We need to determine if a string can become a palindrome after mirror operations.
String contains characters: 'l', 'q', 'b', and other characters.
Mirror operations: 'l' and 'q' become each other, 'b' stays 'b', other characters remain unchanged.
We need to check if we can make the entire string palindrome by possibly changing 'l'<->'q'.

Solution Approach:
1. Find first and last positions of characters that are NOT 'l', 'q', or 'b'.
2. Check if the substring between these positions (inclusive) is palindrome.
3. Check if characters before first special position mirror characters after last special position.
4. If both conditions hold, string can be transformed to palindrome.

Key Insight:
- Only 'l' and 'q' can be swapped, other characters are fixed.
- The fixed characters (not 'l','q','b') must form a palindrome in their positions.
- The remaining positions must have mirror symmetry when accounting for l/q transformations.
*/

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1000010;

int t, n;
char s[N];

// Check if string can be transformed to palindrome
bool check(int l, int r) {
    // If no fixed characters (not 'l','q','b'), always possible
    if (r == -1) return true;
    
    // Check if substring [l, r] is palindrome
    for (int i = l, j = r; i <= j; i++, j--) {
        if (s[i] != s[j]) return false;
    }
    
    // Check mirror symmetry for prefix and suffix around fixed characters
    for (int i = l - 1, j = r + 1; i >= 0; i--, j++) {
        // Check if s[i] and s[j] can be mirror of each other
        if (s[i] == 'l' && s[j] == 'q') continue;
        if (s[i] == 'q' && s[j] == 'l') continue;
        if (s[i] == s[j]) continue;  // Same character (including 'b')
        return false;
    }
    
    return true;
}

void solve() {
    scanf("%s", s);
    n = strlen(s);
    
    // Find first and last positions of characters not 'l', 'q', 'b'
    int first_fixed = n;  // Initialize to beyond end
    int last_fixed = -1;  // Initialize to before start
    
    for (int i = 0; i < n; i++) {
        if (s[i] != 'l' && s[i] != 'q' && s[i] != 'b') {
            first_fixed = min(first_fixed, i);
            last_fixed = max(last_fixed, i);
        }
    }
    
    // Check if transformation to palindrome is possible
    if (check(first_fixed, last_fixed)) {
        puts("Yes");
    } else {
        puts("No");
    }
}

int main() {
    scanf("%d", &t);
    
    while (t--) {
        solve();
    }
    
    return 0;
}
