#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    Solution() : duplicate(-1), missing(-1) {}

    void solve(vector<int> &nums)
    {
      calculate(nums);
    }

    int Duplicate() const {return duplicate;}
    int Missing() const { return missing;}

  private:
    void calculate(vector<int>& nums)
    {
      // edge case : 1 element makes no sense.
      if (nums.size() > 1)
      {
        int size = nums.size();
        int sum = (size * (size + 1)) / 2;
        int product = factorial(size);
        int actualSum = 0;
        int actualProduct = 1;
        for (int i = 0; i < size; i++)
        {
          actualSum += nums[i];
          actualProduct *= nums[i];
        }
        int k1 = actualSum - sum;
        int k2 = actualProduct - product;
        this->duplicate = k1 * actualProduct / k2;
        this->missing = k1 * product / k2;
      }
    }

    int factorial(int n)
    {
      return (n==0 || n==1) ? 1 : n * factorial(n-1);
    }

    int duplicate;
    int missing;
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
    int size, temp;
    vector<int> arr;

    cin >> size;
    while (size != 0)
    {
      cin >> temp;
      arr.push_back(temp);
      size--;
    }

    Solution solution;
    solution.solve(arr);
    cout << solution.Missing() << " " << solution.Duplicate() << endl;
  }
  return 0;
}
