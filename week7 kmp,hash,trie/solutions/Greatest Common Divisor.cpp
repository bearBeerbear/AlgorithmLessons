/*
Problem Analysis:
We need to compute the greatest common divisor (GCD) for multiple pairs of integers.
The GCD of two numbers is the largest positive integer that divides both numbers without remainder.

Solution Approach:
Use Euclid's algorithm (recursive implementation):
1. gcd(a, b) = gcd(b, a mod b)
2. Base case: when b = 0, return a

Complexity Analysis:
- Time: O(log(min(a, b))) per pair (Euclid's algorithm complexity).
- Space: O(log(min(a, b))) for recursion stack depth.

Alternative Approach:
- Iterative implementation available.
- Built-in __gcd() in C++ also works.
*/

#include <iostream>
using namespace std;

int n;

// Recursive Euclidean algorithm for GCD
int gcd(int a, int b) {
    // Base case: if b is 0, a is the GCD
    // Recursive case: gcd(a, b) = gcd(b, a mod b)
    return b ? gcd(b, a % b) : a;
}

int main() {
    cin >> n;
    
    while (n--) {
        int a, b;
        cin >> a >> b;
        
        // Compute and output GCD
        cout << gcd(a, b) << endl;
    }
    
    return 0;
}
