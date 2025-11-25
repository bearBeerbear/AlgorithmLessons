/**
 * Problem: Count Digit Occurrences in Range [a, b]
 * 
 * Approach:
 * 1. Use digit dynamic programming to count occurrences of digits 0-9 in range [1, n]
 * 2. Precompute two DP tables:
 *    - f[i][d]: count of digit d in all i-digit numbers (with leading zeros)
 *    - g[i][d]: count of digit d in all i-digit numbers (without leading zeros)
 * 3. For a given number n, break it into digits and process from most significant to least
 * 4. Count digit occurrences in three parts:
 *    - Numbers with fewer digits than n
 *    - Numbers with same digit prefix but smaller current digit
 *    - The number n itself
 * 
 * Key Functions:
 * - init(): Precompute f and g tables
 * - dp(n): Count digit occurrences from 1 to n
 * - ask(a, b): Count digit occurrences from a to b using prefix sums
 * 
 * Time Complexity: O(log(max(a,b)) per query
 * Space Complexity: O(1) for precomputation
 */

#include <iostream>
#include <vector>

using namespace std;

int base[10];       // base[i] = 10^i
int f[10][10];      // f[i][d]: count of digit d in all i-digit numbers (with leading zeros)
int g[10][10];      // g[i][d]: count of digit d in all i-digit numbers (without leading zeros)

void init()
{
    // Precompute powers of 10
    base[0] = 1;
    for(int i = 1; i <= 9; i++) 
        base[i] = base[i-1] * 10;

    // Initialize f: count for numbers with leading zeros
    for(int i = 0; i <= 9; i++) 
        f[1][i] = 1;  // Single-digit numbers 0-9
    
    for(int i = 2; i <= 9; i++)
        for(int j = 0; j <= 9; j++)
            // For i-digit numbers: 
            // f[i-1][j]*10 - each (i-1)-digit number appears 10 times as prefix
            // base[i-1] - digit j appears in current position for all numbers
            f[i][j] = f[i-1][j] * 10 + base[i-1];

    // Initialize g: count for numbers without leading zeros
    for(int i = 1; i <= 9; i++) 
        g[1][i] = 1;  // Single-digit numbers 1-9
    
    for(int i = 2; i <= 9; i++) {
        // For digit 0: comes from previous count plus 0 in current position
        g[i][0] = g[i-1][0] + f[i-1][0] * 9;
        
        for(int j = 1; j <= 9; j++)
            // For digit j: previous count + j in other positions + j in current position
            g[i][j] = g[i-1][j] + f[i-1][j] * 9 + base[i-1];
    }
}

// Count digit occurrences from 1 to n
vector<int> dp(int n)
{
    vector<int> ans(10, 0); // Store counts for digits 0-9
    if(n <= 0) return ans;  // Boundary case

    // Break n into individual digits (least significant first)
    vector<int> nums;
    while(n) {
        nums.push_back(n % 10);
        n /= 10;
    }

    vector<int> last(10, 0); // Count digits in the current prefix
    
    // Count numbers with fewer digits than n
    for(int i = 0; i <= 9; i++) 
        ans[i] = g[nums.size()-1][i];
    
    // Process from most significant to least significant digit
    for(int i = nums.size()-1; i >= 0; i--) {
        int x = nums[i];  // Current digit
        
        // Count numbers with same prefix but smaller current digit
        int start = (i == nums.size()-1) ? 1 : 0; // First digit cannot be 0
        for(int j = start; j < x; j++) {
            // Count from prefix digits
            for(int k = 0; k <= 9; k++)
                ans[k] += last[k] * base[i];
            
            // Count current digit j
            ans[j] += base[i];
            
            // Count from remaining digits
            for(int k = 0; k <= 9; k++)
                ans[k] += f[i][k];
        }
        
        // Update prefix with current digit
        last[x]++;
        
        // Count the number n itself when we reach the end
        if(i == 0) {
            for(int k = 0; k <= 9; k++)
                ans[k] += last[k];
        }
    }
    
    return ans;
}

// Count digit occurrences from a to b
vector<int> ask(int a, int b)
{
    auto x = dp(b);      // Count from 1 to b
    auto y = dp(a - 1);  // Count from 1 to a-1
    vector<int> ans;
    
    // Subtract to get range [a, b]
    for(int i = 0; i <= 9; i++) 
        ans.push_back(x[i] - y[i]);
    
    return ans;
}

void print(vector<int> ans)
{
    for(auto x : ans) 
        printf("%d ", x);
    puts("");
}

int main()
{
    init();

    int a, b;
    while(cin >> a >> b, a || b) {
        if(a > b) swap(a, b);
        auto t = ask(a, b);
        print(t);
    }

    return 0;
}
