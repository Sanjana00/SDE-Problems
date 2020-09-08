#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    void solve(vector<int>& nums)
    {
      nextPermutation(nums);
      return;
    }

    void print(vector<int>& nums)
    {
      printarr(nums);
      return;
    }

  private:
    void nextPermutation(vector<int>& nums)
    {
      int flag, loc;
      for (flag = nums.size() - 2; flag >= 0; flag--)
        if (nums[flag] < nums[flag + 1])
            break;

      // Case-1 : example -> [6 5 4 3 2 1]
      // entire array is reverse-sorted.
      if (flag == -1)
        reverse(nums.begin(), nums.end());

      // Case-2 : example -> [2 3 6 5 4 1]
      // part of the array is reverse-sorted.
      else
      {
        // swap array[flag] with next greater element.
        for (loc = nums.size() - 1; loc > flag; loc--)
          if (nums[loc] > nums[flag])
            break;

        swap(nums[flag], nums[loc]);

        // reverse the reverse-sorted part of the array.
        reverse(nums.begin() + flag + 1, nums.end());
      }
      return;
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

    cin >> size ;
    while (size != 0)
    {
      cin >> temp;
      arr.push_back(temp);
      size--;
    }

    Solution solution;
    solution.solve(arr);
    solution.print(arr);
  }
  return 0;
}
