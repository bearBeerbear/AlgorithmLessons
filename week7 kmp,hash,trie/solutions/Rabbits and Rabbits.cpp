/*
Problem Analysis:
We need to answer multiple queries comparing whether two substrings of a given string are equal.
String hashing provides an O(1) solution for substring comparison after O(n) preprocessing.

Solution Approach:
1. Precompute hash values for all prefixes of the string using polynomial rolling hash.
2. For each query, compute hash values for both substrings in O(1) time.
3. Compare the hash values to determine if substrings are equal.
4. Use unsigned long long for automatic modulo (2^64 overflow).

Complexity Analysis:
- Preprocessing: O(n)
- Each query: O(1)
- Total: O(n + m) where n is string length, m is number of queries
*/

#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

typedef unsigned long long ULL;
const int N = 1000010;           // Maximum string length
const int base = 131;           // Base for polynomial hash (prime number)

int n, m;                       // n: string length, m: number of queries
char s[N];                      // Input string (1-indexed)
ULL h[N];                       // Hash values for prefixes
ULL p[N];                       // Powers of base for hash computation

// Precompute hash values for all prefixes
void string_hash_prework() {
    p[0] = 1;                   // base^0 = 1
    
    for (int i = 1; i <= n; i++) {
        // Compute hash for prefix [1..i]: h[i] = h[i-1]*base + (s[i]-'a'+1)
        h[i] = h[i - 1] * base + (s[i] - 'a' + 1);
        
        // Compute base^i for future use
        p[i] = p[i - 1] * base;
    }
}

// Get hash value for substring [l, r] (1-indexed)
ULL query(int l, int r) {
    // Hash formula: h[r] - h[l-1] * p[r-l+1]
    return h[r] - h[l - 1] * p[r - l + 1];
}

int main() {
    // Read input string and number of queries
    scanf("%s%d", s + 1, &m);
    
    n = strlen(s + 1);
    
    // Precompute hash values
    string_hash_prework();
    
    // Process each query
    while (m--) {
        int l1, r1, l2, r2;
        scanf("%d%d%d%d", &l1, &r1, &l2, &r2);
        
        // Compare hash values of the two substrings
        if (query(l1, r1) == query(l2, r2)) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
    
    return 0;
}
