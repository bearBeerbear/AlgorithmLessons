/*
Problem Analysis:
We need to count non-overlapping occurrences of pattern string b in text string a.
When a match is found, we cannot reuse any part of that match for future matches.
Standard KMP with reset to 0 after each match achieves this.

Solution Approach:
1. For each test case (until "#" is read as text):
   a. Read pattern b and text a (1-indexed for convenience with KMP).
   b. If text length < pattern length, output 0.
   c. Build KMP prefix/next array for pattern b.
   d. Use KMP search with modification: when full match found (j == m),
      reset j to 0 (not ne[j]) to ensure no overlap, and increment count.
   e. Output count for current test case.

Complexity Analysis:
- Time: O(n + m) per test case (standard KMP).
- Space: O(n + m) for storing strings and prefix array.
*/

#include<bits/stdc++.h>
using namespace std;

// Define maximum size for strings
int const N = 1e6+10;
char a[N], b[N];      // a: text, b: pattern (both 1-indexed)
int ne[N];            // KMP prefix/next array for pattern b

int main(){
    // Process multiple test cases until "#" is encountered
    while(~scanf("%s",a+1)){
        int n, m, s = 0; // n: text length, m: pattern length, s: match count
        
        // Check termination condition (text is "#")
        if(strcmp(a+1, "#")==0) break;
        
        // Read pattern string (1-indexed)
        scanf("%s",b+1);
        
        // Get lengths of text and pattern
        n = strlen(a+1);
        m = strlen(b+1);
        
        // If text is shorter than pattern, no match possible
        if(n < m){
            cout << "0\n";
            continue;
        }
        
        // Build KMP prefix/next array for pattern b
        // ne[i] = length of longest proper prefix of b[1..i] that is also a suffix
        for(int i=2, j=0; i<=m; i++){
            // While mismatch and j > 0, fall back using next array
            while(j && b[i] != b[j+1]) j = ne[j];
            // If characters match, extend prefix length
            if(b[i] == b[j+1]) j++;
            // Record next value for current position
            ne[i] = j;
        }
        
        // KMP search for non-overlapping matches in text a
        for(int i=1, j=0; i<=n; i++){
            // While mismatch and j > 0, fall back using next array
            while(j && a[i] != b[j+1]) j = ne[j];
            // If characters match, extend current match length
            if(a[i] == b[j+1]) j++;
            
            // Full pattern matched
            if(j == m){
                j = 0;    // Reset to start of pattern for non-overlapping matches
                s++;      // Increment match count
            }
        }
        
        // Output result for current test case
        cout << s << '\n';
    }
    
    return 0;
}
