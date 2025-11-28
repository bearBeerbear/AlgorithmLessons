#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1000005;

/**
 * Problem: Find the longest border that appears at least 3 times in the string
 * 
 * Solution Approach:
 * 1. Use KMP to compute the next array for the string
 * 2. The longest border is nxt[n] (longest proper prefix that is also a suffix)
 * 3. Check if this border appears at least 3 times in the string:
 *    - Once at prefix (position 1)
 *    - Once at suffix (position n-k+1)
 *    - At least one more time in the middle
 * 4. If not found, try the next shorter border using nxt[k] chain
 * 5. Continue until a valid border is found or all possibilities exhausted
 */

int t, k, n, nxt[N], f[N];
char c[N], a[N];

// Compute KMP next array for the string
void kmp() {
    for (int i = 2, j = 0; i <= n; i++) {
        while (j > 0 && c[i] != c[j + 1]) j = nxt[j];
        if (c[i] == c[j + 1]) j++;
        nxt[i] = j;
    }
}

// Check if the current border (stored in a[1..k]) appears in the middle of the string
bool find() {
    // Reset f array for new search
    for (int i = 1; i <= n; i++) f[i] = 0;
    
    for (int i = 2, j = 0; i <= n - 1; i++) {  // Search in middle positions (2 to n-1)
        while (j > 0 && c[i] != a[j + 1]) j = f[j];
        if (c[i] == a[j + 1]) j++;
        f[i] = j;
        if (f[i] == k) return true;  // Found the border in middle
    }
    return false;
}

void run() {
    scanf("%s", c + 1);  // Read string starting from index 1
    n = strlen(c + 1);
    
    // Compute KMP next array
    kmp();
    
    // Start with the longest border
    k = nxt[n];
    
    // Special case: entire string is a border of itself
    if (k == n) {
        // Output substring excluding first 2 characters (if possible)
        if (n > 2) {
            for (int i = 3; i <= n; i++) printf("%c", c[i]);
        } else {
            printf("not exist");
        }
        printf("\n");
        return;
    }
    
    // Store the border pattern
    for (int i = 1; i <= k; i++) a[i] = c[i];
    
    // Try all possible borders in decreasing length order
    while (k > 0) {
        if (find()) {
            // Found a border that appears at least 3 times
            for (int i = 1; i <= k; i++) cout << a[i];
            cout << endl;
            return;
        }
        // Try next shorter border
        k = nxt[k];
        // Update border pattern
        for (int i = 1; i <= k; i++) a[i] = c[i];
    }
    
    // No valid border found
    cout << "not exist" << endl;
}

int main() {
    cin >> t;
    while (t--) {
        memset(nxt, 0, sizeof(nxt));
        memset(c, 0, sizeof(c));
        run();
    }
    return 0;
}
