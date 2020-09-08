#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    void solve(vector<vector<int> >& matrix)
    {
      setZeroes(matrix);
      return;
    }

    void print(vector<vector<int> >& matrix)
    {
      printMatrix(matrix);
      return;
    }

  private:
    void setZeroes(vector<vector<int> >& matrix)
    {
      bool setFirstRow = false, setFirstCol = false;

      // set flags.
      for (int i = 0; i < matrix.size(); i++)
        if (matrix[i][0] == 0)
        {
          setFirstCol = true;
          break;
        }

      for (int i = 0; i < matrix[0].size(); i++)
        if (matrix[0][i] == 0)
        {
          setFirstRow = true;
          break;
        }

      for (int i = 1; i < matrix.size(); i++)
        for (int j = 1; j < matrix[0].size(); j++)
          if (matrix[i][j] == 0)
          {
            matrix[i][0] = 0;
            matrix[0][j] = 0;
          }

      // set values based on flags.
      for (int i = 1; i < matrix.size(); i++)
        for (int j = 1; j < matrix[0].size(); j++)
          if (matrix[i][0] == 0 || matrix[0][j] == 0)
            matrix[i][j] = 0;

      if (setFirstRow)
        for (int i = 0; i < matrix[0].size(); i++)
          matrix[0][i] = 0;

      if (setFirstCol)
        for (int i = 0; i < matrix.size(); i++)
          matrix[i][0] = 0;

      return;
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
    int n, m;
    cin >> n >> m;
    vector<vector<int> > matrix;
    for(int i = 0; i < m; i++)
    {
      vector<int> arr;
      for(int j = 0; j < n; j++)
      {
        int temp = 0;
        cin >> temp;
        arr.push_back(temp);
      }
      matrix.push_back(arr);
    }

    Solution solution;
    solution.solve(matrix);
    solution.print(matrix);
  }
  return 0;
}
