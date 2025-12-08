/*
Problem Analysis:
We need to format a list of names with associated processing times into groups (lines)
with maximum group size m. The objective is to minimize the maximum time in any group
(sum of maximum times in each group). This is an optimization problem similar to
paragraph formatting or word wrapping with minimum "badness".

Solution Approach:
Dynamic Programming:
1. best[i] = minimum total maximum time to arrange first i names.
2. group[i] = size of last group ending at position i.
3. Transition: for each possible group size j (1 to m), 
   best[i+j] = min(best[i] + max(time[i..i+j-1])).
4. Reconstruct groups using group[] array.

Complexity Analysis:
- Time: O(n * m) where n is number of names, m is group size limit.
- Space: O(n) for DP arrays.

Key Points:
- Group size cannot exceed m.
- Each group's contribution is the maximum time in that group.
- Need to reconstruct grouping after DP.
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    cin.ignore();  // Ignore newline after reading integers
    
    // Read names and processing times
    vector<string> name(n);
    vector<int> time(n);
    
    for (int i = 0; i < n; i++) {
        getline(cin, name[i]);  // Read name (may contain spaces)
        cin >> time[i];         // Read processing time
        cin.ignore();           // Ignore newline after time
    }
    
    // DP arrays
    vector<int> best(n + 1, INT_MAX);  // best[i] = min total for first i names
    vector<int> group(n + 1, -1);      // group[i] = size of group ending at i
    
    // Base case: 0 names require 0 total time
    best[0] = 0;
    group[0] = 0;
    
    // Dynamic Programming
    for (int i = 0; i <= n; i++) {
        int cur_max = 0;  // Maximum time in current group
        
        // Try group sizes from 1 to m
        for (int j = 1; j <= m && i + j - 1 < n; j++) {
            // Update maximum time in current group
            cur_max = max(cur_max, time[i + j - 1]);
            
            // Update DP if better solution found
            if (best[i] + cur_max < best[i + j]) {
                best[i + j] = best[i] + cur_max;
                group[i + j] = j;  // Store group size
            }
        }
    }
    
    // Output minimum total maximum time
    cout << "Total Time: " << best[n] << endl;
    
    // Reconstruct grouping
    vector<int> groups;
    int pos = n;
    
    // Trace back from end to start
    while (group[pos] != 0) {
        groups.push_back(group[pos]);  // Store group size
        pos -= group[pos];             // Move to previous position
    }
    
    // Output groups in forward order
    reverse(groups.begin(), groups.end());
    
    int name_index = 0;
    for (int group_size : groups) {
        for (int j = 0; j < group_size; j++) {
            cout << name[name_index++] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
