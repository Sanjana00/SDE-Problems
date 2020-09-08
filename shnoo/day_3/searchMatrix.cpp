#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    bool solve(vector<vector<int> >& matrix, int target)
    {
      bool ans = search(matrix, target);
      return ans;
    }

    void print(vector<vector<int> >& matrix)
    {
      printMatrix(matrix);
      return;
    }

  private:
    bool search(vector<vector<int> >& matrix, int target)
    {
      // first find the row using binary search on the first column.
      int low = 0;
      int high = matrix.size() - 1;
      int row = -1;
      while (low <= high)
      {
        int mid = (low + high) / 2;
        if (target == matrix[mid][0])
          return true;
        else if (target > matrix[mid][0])
          low = mid + 1;
        else
          high = mid - 1;;
      }

      // binary search the row found above for the target element.
      row = high;
      low = 0;
      high = matrix[row].size() - 1;
      // high will be -1, if target < matrix[0][0]
      if (row >=0)
      {
        while (low <= high)
        {
          int mid = (low + high) / 2;
          if (target == matrix[row][mid])
            return true;
          else if (target > matrix[row][mid])
            low = mid + 1;
          else
            high = mid - 1;
        }
      }
      return false;
    }

    void printMatrix(vector<vector<int> >& matrix)
    {
      for (int i = 0; i < matrix.size(); i++)
      {
        for (int j = 0; j < matrix[i].size(); j++)
        {
          cout << matrix[i][j] << " ";
        }
        cout << endl;
      }
      cout << endl;
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
    // rows, cols
    int n, m;
    cin >> n >> m;
    vector<vector<int> > matrix;
    int target;
    for(int i = 0; i < n; i++)
    {
      vector<int> arr;
      for(int j = 0; j < m; j++)
      {
        int temp = 0;
        cin >> temp;
        arr.push_back(temp);
      }
      matrix.push_back(arr);
    }
    cin >> target;

    Solution solution;
    cout << solution.solve(matrix, target) << endl;
  }
  return 0;
}
