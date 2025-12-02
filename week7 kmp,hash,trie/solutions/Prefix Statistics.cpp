/*
Problem Analysis:
We need to implement a Trie (prefix tree) to count how many inserted words have a given query string as a prefix.
The problem requires:
1. Insert n words into the Trie.
2. For each of t queries, count the number of inserted words that have the query string as a prefix.

Solution Approach:
1. Build a Trie data structure where each node:
   - Has 26 children pointers for lowercase letters 'a' to 'z'
   - Stores a count (End array) indicating how many words end at that node
2. Insert operation: Traverse the Trie for each character, creating nodes as needed, increment End count at final node.
3. Query operation: Traverse the Trie for query string, sum End counts of all nodes along the path.
   - This counts all words that have the query as prefix (including exact matches).
4. If the query path doesn't exist in Trie, return 0.

Complexity Analysis:
- Time: O(L) per insert/query where L is string length.
- Space: O(N * L * 26) where N is number of words, L is average length.
- Note: tot starts at 1 (node 0 is unused, node 1 is root).
*/

#include <bits/stdc++.h>
using namespace std;

#define fir(i, a, b) for (int i = a; i <= b; i++)  // Loop macro for readability

const int N = 1e6 + 10;       // Maximum total nodes in Trie

char str[N];                  // Buffer for input strings
int trie[N][26];              // Trie structure: trie[node][char] = child node
int End[N];                   // End[node]: count of words ending at this node
int n, t;                     // n: number of words, t: number of queries
int tot = 1;                  // Next available node index (1 is root)

// Insert a word into the Trie
void insert(char a[]) {
    int len = strlen(a);
    int p = 1;  // Start from root (node 1)
    
    fir(i, 0, len - 1) {
        int ch = a[i] - 'a';  // Convert character to index 0-25
        
        // Create new node if path doesn't exist
        if (trie[p][ch] == 0) {
            trie[p][ch] = ++tot;
        }
        
        // Move to child node
        p = trie[p][ch];
    }
    
    // Increment count for words ending at this node
    End[p]++;
}

// Query number of words with given string as prefix
int Search(char a[]) {
    int len = strlen(a);
    int p = 1;      // Start from root (node 1)
    int ans = 0;    // Accumulated count
    
    fir(i, 0, len - 1) {
        int ch = a[i] - 'a';
        
        // Move to child node
        p = trie[p][ch];
        
        // If node doesn't exist, no more words with this prefix
        if (p == 0) {
            return ans;
        }
        
        // Add count of words ending at current node
        ans += End[p];
    }
    
    return ans;
}

int main() {
    // Read number of words and queries
    scanf("%d%d\n", &n, &t);
    
    // Insert all words into Trie
    fir(i, 0, n - 1) {
        scanf("%s\n", str);
        insert(str);
    }
    
    // Process all queries
    while (t--) {
        scanf("%s\n", str);
        printf("%d\n", Search(str));
    }
    
    return 0;
}
