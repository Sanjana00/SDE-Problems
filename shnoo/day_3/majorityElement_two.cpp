#include <bits/stdc++.h>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution
{
  public:
    // Modified Booyer-Moore algorithm
    // http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
    // https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
    // There will be AT MOST 2 majority elements.
    vector<int> findMajority(const vector<int>& nums)
    {
      // find majority elements using the idea from booyer moore algorithm.
      int majorOne = -1;
      int majorTwo = -1;
      int countOne = 0;
      int countTwo = 0;
      for (int i = 0; i < nums.size(); i++)
      {
        if (countOne == 0)
        {
          countOne++;
          majorOne = nums[i];
        }
        else if (countTwo == 0)
        {
          countTwo++;
          majorTwo = nums[i];
        }
        else if (nums[i] == majorOne)
          countOne++;

        else if (nums[i] == majorTwo)
          countTwo++;

        else
        {
          countOne--;
          countTwo--;
        }
      }

      // check whether the elements found above are actually majority elements.
      vector<int> major;
      countOne = 0;
      countTwo = 0;

      for (int i = 0; i < nums.size(); i++)
      {
        if (nums[i] == majorOne)
          countOne++;
        else if (nums[i] == majorTwo)
          countTwo++;
        else
          continue;
      }

      if (countOne > nums.size() / 3)
        major.push_back(majorOne);

      if (countTwo > nums.size() / 3)
        major.push_back(majorTwo);
      return major;
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
    vector<int> ans = solution.findMajority(arr);
    for (int i = 0; i < ans.size(); i++)
      cout << ans[i] << endl;
    cout << "------------" << endl;
  }
  return 0;
}
