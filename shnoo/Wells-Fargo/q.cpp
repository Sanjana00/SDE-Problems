// Question :
// arr - 1 2 3 9
// arr - 1 2 4 4
// pair of numbers which add up to a particular sum.
// sum = 8

/*
// Algo run-through:
1, 7
2, 6
3, 5
9, -1
map - 1, 2, 3, 9

// Pseudo-code:
for (i in arr)
  arr[i]
  search map for value - arr[i]
    return arr[i]
  store the value arr[i] in map

return -1
*/

#include <bits/stdc++.h>

using namespace std;

int pairSum(vector<int>& arr, int value)
{
  if (arr.size() < 0)
  {
    cout << "Arr is empty" << endl;
    return -1;
  }

  map<int, int> x;
  int count = 0;

  map<int, int>::iterator itr;

  for (int i = 0; i < arr.size(); ++i)
  {
    itr = x.find(value - arr[i]);
    if (itr == x.end())
    {
      x[arr[i]] = count;
      count++;
    }
    else
    {
      cout << value - arr[i] << " " << arr[i] << endl;
    }
  }
  return 0;
}

int main()
{
  int size;
  cin >> size;
  int value;
  cin >> value;
  vector<int> arr;
  for (int i = 0; i < size; ++i)
  {
    int temp;
    cin >> temp;
    arr.push_back(temp);
  }
  // x will signal if the input has an empty array
  // or if function executed correctly.
  int x = pairSum(arr, value);
  return 0;
}
