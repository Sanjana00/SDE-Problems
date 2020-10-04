#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    // dp[i][0] = dp[0][j] = 1 (base case)
    // dp[i][j] = dp[i-1][j] + dp[i][j-1] (recursive case)
    int findUniquePaths(const int& m, const int& n)
    {
      // base case
      vector<vector<int> > dp(m, vector<int>(n, 1));

      // recursive case
      for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
          dp[i][j] = dp[i][j-1] + dp[i-1][j];

      return dp[m-1][n-1];
    }
};

int main(int argc, char* argv[])
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  cin >> T;

  for(int i = 0; i < T; i++)
  {
    int m, n;
    cin >> m >> n;

    Solution solution;
    int ans = solution.findUniquePaths(m, n);
    cout << ans << endl;
  }
  return 0;
}
