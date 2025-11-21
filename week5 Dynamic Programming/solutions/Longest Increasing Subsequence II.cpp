#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <climits>

#define KL puts("");
#define x first
#define y second
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;

const int mod=1e9+7,N=1e5+10;
int n,q[N],a[N];

// Problem: Find length of longest strictly increasing subsequence
// Approach: Greedy + Binary Search
// Key idea: Maintain an array q where q[i] = smallest ending value for all increasing subsequences of length i
// For each new element a[i], use binary search to find the largest q[j] < a[i]
// Then update q[j+1] = min(q[j+1], a[i]) to maintain the greedy property
// Result: The length of q array (largest index with valid value)

void work()
{
	cin>>n;
	for(int i=1;i<=n;i++)scanf("%d",&a[i]);
	
	int len=0;
	q[0]=-2e9;  // Initialize with very small number as sentinel
	
	for(int i=1;i<=n;i++)
	{
	    int l=0,r=len;
	    // Binary search to find the largest q[j] < a[i]
	    while(l<r)
	    {
	        int mid=l+r+1>>1;
	        if(q[mid]<a[i])l=mid;
	        else r=mid-1;
	    }
	    // Update maximum length if needed
	    len=max(len,r+1);
	    // Update q[r+1] with current value (maintains smallest ending for length r+1)
	    q[r+1]=a[i];
	}
    cout<<len;
}

int main()
{
    int T=1;
    //scanf("%d",&T);
    while(T--)work();
    return 0;
}