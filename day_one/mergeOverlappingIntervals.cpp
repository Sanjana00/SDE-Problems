#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    Solution() : j(0) {};

    void solve(vector<pair <int, int> > &nums)
    {
      mergeOverlappingSpaceOptimized(nums);
      //mergeOverlapping(nums);
      return;
    }

    void print(vector<pair <int, int> > &nums)
    {
      printarr(nums, this->j);
      //printarr(nums);
      return;
    }

  private:
    // O(NlogN + N) time, O(1) space.
    // modifies the input array in-place during traversal.
    void mergeOverlappingSpaceOptimized(vector<pair <int, int> >& nums)
    {
      sort(nums.begin(), nums.end());
      pair<int, int> val;
      for (int i = 1; i < nums.size(); i++)
      {
        if (nums[i].first < nums[this->j].second)
        {
          val.first = min(nums[i].first, nums[this->j].first);
          val.second = max(nums[i].second, nums[this->j].second);
          nums[this->j] = val;
        }
        else
        {
          this->j++;
          nums[this->j] = nums[i];
        }
      }
      return;
    }

    // O(NlogN + N) time, O(N) space.
    // calculates the modified temporary array and assigns it to the input.
    void mergeOverlapping(vector<pair <int, int> >& nums)
    {
      sort(nums.begin(), nums.end());
      // behaves like a stack.
      vector<pair <int, int> > temp;
      temp.push_back(nums[0]);
      pair<int, int> val;
      for (int i = 1, j = 0; i < nums.size(); i++)
      {
        // modify the stack top by merging overlapping intervals.
        if (nums[i].first < temp[j].second)
        {
          val.first = min(nums[i].first, temp[j].first);
          val.second = max(nums[i].second, temp[j].second);
          temp[j] = val;
        }
        // push to stack.
        else
        {
          temp.push_back(nums[i]);
          j++;
        }
      }
      nums = temp;
      return;
    }

    void printarr(vector<pair <int, int> > &nums, int reducedSize = INT_MAX)
    {
      if(reducedSize != INT_MAX)
      {
        for(int i = 0; i <= reducedSize; i++)
        {
          cout << "{" << nums[i].first << "," << nums[i].second << "} ";
        }
        cout << endl;
      }
      else
      {
        for (int i = 0; i < nums.size(); i++)
        {
          cout << "{" << nums[i].first << "," << nums[i].second << "} ";
        }
        cout << endl;
      }
      return;
    }

    int j;
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
    int size, first, second;
    pair <int, int> val;
    vector<pair <int, int> > arr;

    cin >> size;
    while (size != 0)
    {
      cin >> first >> second;
      val = make_pair(first, second);
      arr.push_back(val);
      size--;
    }

    Solution solution;
    solution.solve(arr);
    solution.print(arr);
  }
  return 0;
}
