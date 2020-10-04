#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    // Booyer-Moore algorithm
    // http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
    // https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
    // This explicitly assumes that there is a majority element.
    int findMajority(const vector<int>& nums)
    {
      int major = -1;
      int count = 0;
      for (int i = 0; i < nums.size(); i++)
      {
        if (count == 0)
        {
          count++;
          major = nums[i];
        }
        else if (nums[i] == major)
          count++;
        else
          count--;
      }
      return major;
    }

    int findMajorityHashMap(const vector<int>& nums)
    {
      unordered_map<int, int> m;
      for (int i = 0; i < nums.size(); i++)
      {
        auto it = m.find(nums[i]);
        if (it == m.end())
          m.insert(make_pair(nums[i],1));
        else
          m[nums[i]]++;
      }

      for (auto it : m)
      {
        if (it.second > nums.size()/2)
          return it.first;
      }

      // returns -1 if there are no majority elements
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
    int ans = solution.findMajority(arr);
    cout << ans << endl;
  }
  return 0;
}
