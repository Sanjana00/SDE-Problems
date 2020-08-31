#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    // in-place algorithm.
    void sort012(vector<int>& nums)
    {
      int low = 0;
      int mid = 0;
      int high = nums.size() - 1; // O(1) time.
      // O(N) time.
      while (mid <= high)
      {
        if (nums[mid] == 0)
        {
          swap(nums[low], nums[mid]);
          low++;
          mid++;
        }
        else if (nums[mid] == 1)
        {
          mid++;
        }
        else
        {
          swap(nums[mid], nums[high]);
          high--;
        }
      }
      return;
    }

    void print(vector<int> &nums)
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
    solution.sort012(arr);
    solution.print(arr);
  }
  return 0;
}
