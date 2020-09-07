#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int solve(vector<int>& nums)
    {
      return mergeSortAndCount(nums, 0, nums.size() - 1);
    }

    void print(vector<int>& nums)
    {
      printarr(nums);
      return;
    }

  private:
    void merge(vector<int>& nums, int start, int mid, int end)
    {
      int n1 = (mid - start + 1);
      int n2 = (end - mid);
      int L[n1], R[n2];

      for (int i = 0; i < n1; i++)
        L[i] = nums[start + i];

      for (int j = 0; j < n2; j++)
        R[j] = nums[mid + 1 + j];

      for (int i = 0, j = 0, k = start; k <= end; k++)
      {
        if (j >= n2 || (i < n1 && L[i] <= R[j]))
          nums[k] = L[i++];
        else
          nums[k] = R[j++];
      }
      return;
    }

    int mergeSortAndCount(vector<int>& nums, int start, int end)
    {
      int count = 0;
      if (start < end)
      {
        int mid = (start + end) / 2;

        // inversions for nums[start...mid]
        count += mergeSortAndCount(nums, start, mid);

        // inversions for nums[mid+1...end]
        count += mergeSortAndCount(nums, mid + 1, end);

        // inversions between nums[start...mid] and nums[mid+1...end]
        int j = mid + 1;
        for (int i = start; i <= mid; i++)
        {
          while (j <= end && nums[i] > nums[j])
            j++;
          count += j - (mid + 1);
        }
        merge(nums, start, mid, end);
        return count;
      }
      else
        return count;
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
    cout << solution.solve(arr) << endl;
  }
  return 0;
}
