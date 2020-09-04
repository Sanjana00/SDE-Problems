#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
  public:
    vector<vector<int> > solve(int numRows)
    {
      vector<vector<int> > pascal(numRows, vector<int>());
      pascal = generateBinomial(numRows);
      //pascal = generateDirectly(numRows);
      return pascal;
    }

    void print(vector<vector<int> >& matrix)
    {
      printMatrix(matrix);
      return;
    }

  private:
    // supposedly, kind of a DP solution, but anyway :)
    vector<vector<int> > generateDirectly(int numRows)
    {
      vector<vector<int> > pascal(numRows, vector<int>());
      // for 0 rows, just return an empty matrix.
      if (numRows > 0)
      {
        for (int i = 0; i < numRows; i++)
        {
          for (int j = 0; j < i + 1; j++)
          {
            if (j == 0 || j == i)
              pascal[i].push_back(1);
            else
              pascal[i].push_back(pascal[i-1][j-1] + pascal[i-1][j]);
          }
        }
      }
      return pascal;
    }

    // using Binomial theorem
    vector<vector<int> > generateBinomial(int numRows)
    {
      vector<vector<int> > pascal(numRows, vector<int>());
      // for 0 rows, just return an empty matrix.
      if (numRows > 0)
      {
        for (int i = 0; i < numRows; i++)
        {
          for (int j = 0; j < i + 1; j++)
          {
            if (j == 0 || j == i)
              pascal[i].push_back(1);
            else
              pascal[i].push_back(nCr(i,j));
          }
        }
      }
      return pascal;
    }

    int factorial(int n)
    {
      return (n == 0 || n == 1) ? 1 : n * factorial(n - 1);
    }

    int nCr(int n, int r)
    {
      return factorial(n) / (factorial(r) * factorial(n-r));
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
    int rows;
    cin >> rows;

    Solution solution;
    vector<vector<int> > pascal = solution.solve(rows);
    solution.print(pascal);
  }
  return 0;
}
