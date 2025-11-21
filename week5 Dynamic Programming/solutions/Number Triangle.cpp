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

const int mod=1e9+7,N=5e2+10;
int n;
int a[N][N];
int f[N][N];

// Problem: Find maximum path sum in a number triangle from top to bottom
// Approach: Dynamic Programming from top to bottom
// State: f[i][j] = maximum sum reaching position (i,j)
// Transition: f[i][j] = max(f[i-1][j], f[i-1][j-1]) + a[i][j]
// Base case: f[1][1] = a[1][1]
// Result: max(f[n][j]) for all j in last row

void work()
{
	cin>>n;
	for(int i=1;i<=n;i++)
	    for(int j=1;j<=n;j++)
	        if(j<=i)
	        {
	            cin>>a[i][j];
	            // For first column, can only come from above
	            if(j==1) f[i][j]=f[i-1][j]+a[i][j];
	            // For last element in row, can only come from upper left
	            else if(i==j) f[i][j]=f[i-1][j-1]+a[i][j];
	            // For middle elements, choose maximum from above left or above
	            else f[i][j]=max(f[i-1][j],f[i-1][j-1])+a[i][j];
	        }
	int ans=-2e9;
	// Find maximum value in bottom row
	for(int i=1;i<=n;i++) ans=max(ans,f[n][i]);
	cout<<ans<<endl;
}

int main()
{
    int T=1;
    //scanf("%d",&T);
    while(T--)work();
    return 0;
}