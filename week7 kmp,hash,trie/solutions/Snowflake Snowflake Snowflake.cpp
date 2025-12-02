/*
Problem Analysis:
We need to determine if there are any identical snowflakes among n given snowflakes.
Each snowflake is represented by 6 integer values in a circle.
Two snowflakes are identical if one can be rotated (clockwise or counterclockwise) to match the other.

Solution Approach:
1. Use hash table to store snowflakes efficiently.
2. For each snowflake, compute a hash value based on sum and product of its 6 values modulo a prime.
3. Use separate chaining (linked list) for collision resolution.
4. When inserting a new snowflake:
   - Compute its hash value.
   - Check all snowflakes in the same bucket for equality using rotation comparison.
   - If found identical, output result immediately.
5. Comparison function checks all possible starting points and both directions.

Complexity Analysis:
- Time: O(n) on average (good hash distribution).
- Worst case: O(n^2) if all snowflakes hash to same bucket.
- Space: O(n) for storing snowflakes.
*/

#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1e5 + 10;    // Maximum number of snowflakes
const int P = 92083;       // Prime number for hash table size

int n;                     // Number of snowflakes
int tot;                   // Total snowflakes stored
int snow[N][6];            // Store snowflake data
int head[P];               // Hash table heads
int nxt[N];                // Next pointers for linked list
int tmp[6];                // Temporary storage for current snowflake

// Compute hash value for a snowflake
// Hash = (sum of values + product of values) mod P
int get_hash(int* a) {
    int sum = 0;
    ll product = 1;        // Use long long to avoid overflow
    
    for (int i = 0; i < 6; i++) {
        sum = (sum + a[i]) % P;
        product = product * a[i] % P;
    }
    
    return (sum + product) % P;
}

// Check if two snowflakes are identical
bool check(int* a, int* b) {
    // Try all starting points in snowflake a
    for (int start_a = 0; start_a < 6; start_a++) {
        // Try all starting points in snowflake b
        for (int start_b = 0; start_b < 6; start_b++) {
            
            // Check clockwise direction
            bool flag = true;
            for (int k = 0; k < 6; k++) {
                if (a[(start_a + k) % 6] != b[(start_b + k) % 6]) {
                    flag = false;
                    break;
                }
            }
            if (flag) return true;
            
            // Check counterclockwise direction
            flag = true;
            for (int k = 0; k < 6; k++) {
                if (a[(start_a + k) % 6] != b[(start_b - k + 6) % 6]) {
                    flag = false;
                    break;
                }
            }
            if (flag) return true;
        }
    }
    
    return false;
}

// Insert a snowflake into hash table
// Returns true if identical snowflake found, false otherwise
bool insert(int* a) {
    int hval = get_hash(a);  // Compute hash value
    
    // Check all snowflakes in the same bucket
    for (int i = head[hval]; i; i = nxt[i]) {
        if (check(snow[i], a)) {
            return true;  // Found identical snowflake
        }
    }
    
    // No identical snowflake found, insert new one
    tot++;
    for (int i = 0; i < 6; i++) {
        snow[tot][i] = a[i];
    }
    // Insert at head of linked list for bucket hval
    nxt[tot] = head[hval];
    head[hval] = tot;
    
    return false;
}

int main() {
    scanf("%d", &n);
    
    while (n--) {
        // Read current snowflake
        for (int i = 0; i < 6; i++) {
            scanf("%d", &tmp[i]);
        }
        
        // Try to insert, if duplicate found, output and exit
        if (insert(tmp)) {
            printf("Twin snowflakes found.\n");
            return 0;
        }
    }
    
    // No duplicates found
    printf("No two snowflakes are alike.\n");
    return 0;
}
