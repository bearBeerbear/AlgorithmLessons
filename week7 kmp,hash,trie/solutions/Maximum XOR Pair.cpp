/*
Problem Analysis:
We need to find the maximum XOR pair among n integers.
For each number x, we want to find another number y in the set that maximizes x XOR y.
Brute force O(n^2) is too slow for n up to 100,000.

Solution Approach:
1. Use Trie (binary tree) to store binary representations of numbers (from most to least significant bit).
2. For each number x:
   a. Insert x into Trie.
   b. Query Trie to find number y that maximizes x XOR y:
      - For each bit from MSB to LSB, try to go opposite direction of x's bit.
      - If opposite child exists, go there (this maximizes XOR).
      - Otherwise, go same direction.
3. Track maximum XOR value found.

Complexity Analysis:
- Time: O(n * 32) where 32 is number of bits (for 32-bit integers).
- Space: O(n * 32) for Trie nodes.
*/

#include <iostream>
#include <algorithm>
using namespace std;

const int N = 100010;
const int BIT_LENGTH = 32;  // For 32-bit integers

// Trie for binary numbers: each node has 2 children (0 and 1)
int son[N * BIT_LENGTH][2];
int n, idx;  // idx: next available node index (0 is root)

// Insert integer x into Trie (store its binary representation)
void insert(int x) {
    int p = 0;  // Start from root
    
    // Process bits from most significant to least significant
    for (int i = BIT_LENGTH - 1; i >= 0; i--) {
        int u = (x >> i) & 1;  // Extract i-th bit
        
        // Create new node if path doesn't exist
        if (!son[p][u]) {
            son[p][u] = ++idx;
        }
        
        // Move to child node
        p = son[p][u];
    }
}

// Find number in Trie that maximizes XOR with x
int query(int x) {
    int p = 0;      // Start from root
    int result = 0; // Will store the number that maximizes XOR
    
    // Process bits from most significant to least significant
    for (int i = BIT_LENGTH - 1; i >= 0; i--) {
        int u = (x >> i) & 1;  // Extract i-th bit of x
        
        // Prefer opposite bit to maximize XOR
        if (son[p][!u]) {
            // Go to opposite bit child
            p = son[p][!u];
            // Update result with opposite bit
            result = result * 2 + !u;
        } else {
            // Opposite not available, go with same bit
            p = son[p][u];
            // Update result with same bit
            result = result * 2 + u;
        }
    }
    
    // Return XOR value (result ^ x)
    return result ^ x;
}

int main() {
    cin >> n;
    int maxXor = 0;  // Maximum XOR value found
    
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        
        // First insert, then query (excluding x itself)
        // Note: query(x) will find best match among previously inserted numbers
        // This ensures we don't compare x with itself
        if (i > 0) {  // Skip query for first element
            maxXor = max(maxXor, query(x));
        }
        insert(x);
    }
    
    cout << maxXor << endl;
    return 0;
}
