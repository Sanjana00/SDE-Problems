#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int solve(vector<int> &nums)
    {
      int ans = INT_MIN;
      ans = maxProfit(nums);
      return ans;
    }

  private:

    // maps the input to the max subarray problem.
    int maxProfit(vector<int>& nums)
    {
      vector<int> profits (nums.size(), 0);
      for (int i = 1; i < profits.size(); i++)
        profits[i] = nums[i] - nums[i - 1];
      return maxSumSubArr(profits);
    }

    // Kadane's algorithm - O(n)
    int maxSumSubArr(vector<int>& nums)
    {
      if (nums.size() == 0)
        return 0;
      else if (nums.size() == 1)
        return nums[0];
      else
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
    }

    void printarr(vector<int> &nums)
    {
      for (int i = 0; i < nums.size(); i++)
      {
        cout << nums[i] << " ";
      }
      cout << endl;
      return;
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
