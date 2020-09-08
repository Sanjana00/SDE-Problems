/**
  * clockwise rotate - Method 1:
  * first transpose, then reverse left to right

  * 1 2 3  Transpose  1 4 7  Reverse 7 4 1
  * 4 5 6 ==========> 2 5 8 =======> 8 5 2
  * 7 8 9             3 6 9          9 6 3
  *
  *
  * clockwise rotate - Method 2:
  * first reverse up to down, then transpose
  * 1 2 3     7 8 9     7 4 1
  * 4 5 6  => 4 5 6  => 8 5 2
  * 7 8 9     1 2 3     9 6 3
  *
  */

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    void solve(vector<vector<int> >& matrix)
    {
      rotateClockwise(matrix);
      return;
    }

    void print(vector<vector<int> >& matrix)
    {
      printMatrix(matrix);
      return;
    }

  private:
    // follows method 1
    void rotateClockwise(vector<vector<int> >& matrix)
    {
      // first transpose
      Transpose(matrix);

      // then reverse each row from left to right
      for (int i = 0; i < matrix.size(); i++)
        reverse(matrix[i].begin(), matrix[i].end());

      return;
    }

    void Transpose(vector<vector<int> >& matrix)
    {
      for (int i = 0; i < matrix.size(); i++)
        for (int j = i + 1; j < matrix[i].size(); j++)
          swap(matrix[i][j], matrix[j][i]);
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
