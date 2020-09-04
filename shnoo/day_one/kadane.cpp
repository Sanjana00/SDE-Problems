#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int solve(vector<int> &nums)
    {
      int ans = -1;
      // edge case : empty array
      if (nums.size() > 0)
        ans = maxSumSubArr(nums);
      return ans;
    }

  private:
    // Kadane's algorithm - O(n)
    int maxSumSubArr(vector<int>& nums)
    {
      int localMax = nums[0];
      int globalMax = nums[0];
      for (int i = 1; i < nums.size(); i++)
      {
        localMax = max(nums[i], localMax + nums[i]);
        if (localMax > globalMax)
          globalMax = localMax;
      }
      return globalMax;
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
    cout << solution.solve(arr) << endl;
  }
  return 0;
}
