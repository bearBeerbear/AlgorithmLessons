#include <iostream>
using namespace std;

const int N = 1e3 + 10;

char a[N], b[N];
int f[N][N];  // f[i][j] represents minimum operations to convert first i chars of A to first j chars of B

// Problem: Find minimum edit distance between two strings (Levenshtein distance)
// Approach: Dynamic Programming
// State: f[i][j] = min operations to convert A[1..i] to B[1..j]
// Operations: delete, insert, replace
// Transition:
//   - Delete: f[i-1][j] + 1 (remove last char from A)
//   - Insert: f[i][j-1] + 1 (add last char of B to A)
//   - Replace: if chars match: f[i-1][j-1], else: f[i-1][j-1] + 1
// Base cases:
//   - f[i][0] = i (delete all i chars from A to get empty string)
//   - f[0][j] = j (insert all j chars into empty string to get B)

int main()
{
    int n, m;
    scanf("%d%s%d%s", &n, a + 1, &m, b + 1);

    // Initialize base cases
    for (int i = 1; i <= n; i++) f[i][0] = i;  // Delete all characters from A
    for (int i = 1; i <= m; i++) f[0][i] = i;  // Insert all characters into empty string

    // Fill DP table
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
        {
            // Option 1: Delete last character from A
            // Option 2: Insert last character of B into A
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1);

            // Option 3: Replace (or keep if characters match)
            if (a[i] == b[j]) {
                // Characters match, no operation needed
                f[i][j] = min(f[i][j], f[i - 1][j - 1]);
            } else {
                // Characters differ, need replace operation
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1);
            }
        }

    cout << f[n][m];
    return 0;
}