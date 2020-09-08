#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    double solve(double x, int n)
    {
      return Pow(x, n);
    }

  private:
    double Pow(double x, int n)
    {
      double ans = 0;

      // Avoiding Integer Overflow using this.
      long long p;
      if (n < 0)
      {
        p = (-1LL) * n;
        x = 1.0 / x;
      }
      else
      {
        p = n;
      }

      ans = recursion(x, p);
      return ans;
    }

    // 0ms runtime solution.
    double recursion(double x, long long n)
    {
      if (n == 0)
        return 1;
      return (n % 2 == 0) ? pow(x * x, n / 2) : x * pow(x * x, n / 2);
    }

    double iterative(double x, long long n)
    {
      double ans = 1.0;
      while (n)
      {
        // if n is odd
        if (n & 1)
          ans *= x;
        x *= x;
        n >>= 1;
      }
      return ans;
    }

    // This gives TLE when n is too large.
    double dnq(double x, long long n)
    {
      if (n == 0)
        return 1;
      if (n == 1)
        return x;
      return dnq(x, n / 2) * dnq(x, (n / 2 + n % 2));
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
    double x;
    int n;
    cin >> x >> n;
    Solution solution;
    cout << solution.solve(x, n) << endl;
  }
  return 0;
}
