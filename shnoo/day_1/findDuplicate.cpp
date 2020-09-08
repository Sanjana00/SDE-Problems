#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int findDuplicate(vector<int>& nums)
    {
      // edge case : single element means no duplicates.
      if (nums.size() > 1)
      {
        int slow = 0;
        int fast = 0;
        int find = 0;
        // detect a cycle.
        while (true)
        {
          slow = nums[slow];
          fast = nums[nums[fast]];
          if (slow == fast)
            break;
        }
        // find starting point of cycle.
        while (true)
        {
          slow = nums[slow];
          find = nums[find];
          if (slow == find)
            break;
        }
        return slow;
      }
      return -1;
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
    int ans = solution.findDuplicate(arr);
    cout << ans << endl;
  }
  return 0;
}
