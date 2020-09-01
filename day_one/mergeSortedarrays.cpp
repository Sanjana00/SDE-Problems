#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    void solve(vector<int> &nums1, vector<int> &nums2)
    {
      calculate(nums1, nums2);
      //calculateNonOptimal(nums1, nums2);
      return;
    }

    void print(vector<int> &nums)
    {
      printarr(nums);
      return;
    }

  private:
    int Gap(int n)
    {
      return (n <= 1) ? 0 : ((n / 2) + (n % 2));
    }

    // Gap Method - Based on Shell Sort algo.
    void calculate(vector<int>& nums1, vector<int> &nums2)
    {
      int size = nums1.size() + nums2.size();
      int gap = Gap(size);

      // p1 iterates over first array and p2 iterates over second array.
      int p1, p2;
      while(gap >= 1)
      {
        // left array
        for (p1 = 0; p1 + gap < nums1.size(); p1++)
          if (nums1[p1] > nums1[p1 + gap] )
            swap(nums1[p1], nums1[p1 + gap]);

        // between arrays
        p2 = p1 + gap - nums1.size();
        for (; p1 < nums1.size() && p2 < nums2.size() ; p1++, p2++)
          if (nums1[p1] > nums2[p2])
            swap(nums1[p1], nums2[p2]);

        // right array
        if (p2 < nums2.size())
          for (p2 = 0; p2 + gap < nums2.size(); p2++)
            if (nums2[p2] > nums2[p2 + gap])
              swap(nums2[p2], nums2[p2+gap]);

        gap = Gap(gap);
      }
    }

    // Based on Insertion Sort algo.
    void calculateNonOptimal(vector<int>& nums1, vector<int> &nums2)
    {
      // sort the first array one element at a time,
      // while keeping the second always sorted.
      for(int p1 = 0; p1 < nums1.size(); p1++)
        if (nums1[p1] > nums2[0])
        {
          swap(nums1[p1], nums2[0]);

          // keep second array always sorted,
          // if first element becomes out of order.
          if (nums2[0] > nums2[1])
            InsertionSort(nums2);
        }
      return;
    }

    // best [O(n)] algo for when only one element is not sorted in the array.
    void InsertionSort(vector<int>& nums)
    {
      int key, j;
      for (int i = 1; i < nums.size(); i++)
      {
        key = nums[i];
        j = i - 1;
        for (; j >=0 && nums[j] > key; j--)
          swap(nums[j + 1], nums[j]);
        nums[j + 1] = key;
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
    int size1, size2, temp;
    vector<int> arr1;
    vector<int> arr2;

    cin >> size1 >> size2;
    while (size1 != 0)
    {
      cin >> temp;
      arr1.push_back(temp);
      size1--;
    }

    while (size2 != 0)
    {
      cin >> temp;
      arr2.push_back(temp);
      size2--;
    }

    Solution solution;
    solution.solve(arr1, arr2);
    solution.print(arr1);
    solution.print(arr2);
  }
  return 0;
}
