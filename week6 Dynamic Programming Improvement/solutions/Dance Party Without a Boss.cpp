/**
 * Problem: Maximum Happiness in Company Hierarchy (Tree DP)
 * 
 * Approach:
 * 1. Model the company structure as a tree where edges represent supervisor-subordinate relationships
 * 2. Use tree dynamic programming with states:
 *    - f[u][0]: maximum happiness when node u is NOT attended
 *    - f[u][1]: maximum happiness when node u IS attended
 * 3. Perform DFS traversal to compute DP values bottom-up
 * 
 * Key Constraints:
 * - No employee attends with their direct supervisor
 * - If a supervisor attends, their direct subordinates cannot attend
 * - If a supervisor doesn't attend, subordinates may or may not attend
 * 
 * Recurrence Relations:
 * f[u][0] = ¦² max(f[child][0], f[child][1])  // u not attended: children free to choose
 * f[u][1] = happy[u] + ¦² f[child][0]         // u attended: children cannot attend
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */

#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 6010;

int n;
int happy[N];           // Happiness index for each employee
int f[N][2];            // DP table: f[u][0] - not attend, f[u][1] - attend

// Adjacency list for tree representation
int e[N], ne[N], h[N], idx;
bool has_father[N];     // Track if node has a parent (to find root)

// Add edge from a to b (a is supervisor of b)
void add(int a, int b) {
    e[idx] = b;         // Store destination node
    ne[idx] = h[a];     // Point to current head
    h[a] = idx++;       // Update head pointer
}

void dfs(int u) {
    // Base case: if u attends, include its happiness
    f[u][1] = happy[u];
    
    // Process all children of u
    for (int i = h[u]; i != -1; i = ne[i]) {
        int j = e[i];   // Child node
        dfs(j);         // Recursively process child
        
        // State transitions:
        // If u doesn't attend, children can choose to attend or not
        f[u][0] += max(f[j][0], f[j][1]);
        // If u attends, children cannot attend
        f[u][1] += f[j][0];
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) 
        scanf("%d", &happy[i]);
    
    // Initialize adjacency list
    memset(h, -1, sizeof h);
    
    // Build tree structure
    for (int i = 1; i < n; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        has_father[a] = true;  // a has a supervisor
        add(b, a);             // b is supervisor of a
    }
    
    // Find root node (the one without supervisor)
    int root = 1;
    while (has_father[root]) 
        root++;
    
    // Perform DFS from root to compute DP values
    dfs(root);
    
    // Answer is maximum of root attending or not attending
    printf("%d\n", max(f[root][0], f[root][1]));
    
    return 0;
}
