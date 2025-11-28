#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<unordered_set>
using namespace std;

/**
 * Problem: Count distinct anagrams of string s1 in string s2
 * 
 * Solution Approach:
 * 1. Use sliding window of size s1.length() over s2
 * 2. For each window, check if it's an anagram of s1 by comparing character frequencies
 * 3. Use rolling hash to efficiently identify distinct substrings
 * 4. Use unordered_set to store hashes of distinct anagrams
 * 5. Count unique anagrams found in s2
 * 
 * Steps:
 * - Precompute character frequencies for s1
 * - Use sliding window to maintain frequencies for current window in s2
 * - Compare frequencies to check for anagram
 * - Use polynomial rolling hash for substring identification
 * - Store unique hashes in set to count distinct anagrams
 */

typedef unsigned long long ULL;
const int N = 150, M = 2e5 + 10, P = 131;
unordered_set<ULL> S;  // Store hashes of distinct anagrams found
ULL p[M], h[M];        // Power array and hash prefix array
int cnt1[N], cnt2[N];  // Character frequency counters for s1 and current window

// Get substring hash using polynomial rolling hash
ULL get_hash(int l, int r)
{
    return h[r] - h[l - 1] * p[r - l + 1];
}

int main()
{
//	freopen("006.1.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
    string s1, s2;
    cin >> s1 >> s2;

    int n = s1.size(), m = s2.size();
    
    // Count character frequencies in s1
    for(int i = 0; i < s1.size(); i ++) 
        cnt1[s1[i]] ++;
    
    // Initialize frequency count for first window in s2
    for(int i = 0; i < min(n, m); i ++) 
        cnt2[s2[i]] ++;

    // Precompute power array and hash prefix array for s2
    p[0] = 1;
    for(int i = 1; i <= m; i ++)
    {
        p[i] = p[i - 1] * P;                    // Precompute powers
        h[i] = h[i - 1] * P + s2[i - 1];       // Build hash prefix
    }

    int res = 0;  // Count of distinct anagrams
    
    // Slide window of size n over s2
    for(int i = 0; i + n <= m; i ++)
    {
        // Update frequency counts for current window
        if(i)  // Skip for first window (already initialized)
        {
            cnt2[s2[i - 1]] --;           // Remove leftmost character
            cnt2[s2[i + n - 1]] ++;       // Add new rightmost character
        }

        // Check if current window is an anagram of s1
        bool flag = true;
        for(char c = 'a'; c <= 'z'; c ++)
            if(cnt1[c] != cnt2[c]) 
            {
                flag = false;
                break;
            }

        // If anagram found and not already counted
        ULL hash = get_hash(i + 1, i + n);  // Get hash of current window
        if(flag && !S.count(hash)) 
        {
            res ++;
            S.insert(hash);  // Mark this anagram as seen
        }
    }

    printf("%d", res);
    return 0;
}
