//binarySearch array

#include <iostream>

using namespace std;

int
binarySearch (int arr[], int n, int num)
{
  int s = 0;
  int e = n;
  while (s <= e)
    {
      int mid = (s + e) / 2;

      if (arr[mid] == num)
	{
	  return mid;
	}
      else if (arr[mid] > num)
	{
	  e = mid - 1;
	}
      else
	{
	  s = mid + 1;
	}
    }
  return -1;
}

int
main ()
{

  int n, num, x;
  cout << "Enter the no of elements: ";
  cin >> n;

  int arr[n];
  cout << "\nEnter the array(Sorted): ";
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  cout << "\nEnter the number: ";
  cin >> num;

  x = binarySearch (arr, n, num);
  
  if(x!=-1)
    cout<<"\nThe no. is present at "<<x<<" index";
  else
    cout<<"\nNot found"; 

  return 0;
}




//delete from an array

using namespace std;

int
Delete (int arr[], int n, int x)
{
    int i,count=0;

 for(i=0; i<n; i++)
        {
                if(arr[i]==x)
                {
                        for(int j=i; j<(n-1); j++)
                        {
                                arr[j]=arr[j+1];
                        }
                        count++;
                        break;
                }
        }
        if(count==0)
        {
                cout<<"\nElement not found\n";
        }
        else
        {
                cout<<"\nElement deleted successfully\n";
                cout<<"\nNow the new array is: ";
                for(i=0; i<(n-1); i++)
                {
                        cout<<arr[i]<<" ";
                }
        }

}

int
main ()
{

  int x, position, n, arr[n];

  cout << "Enter the no of elements: ";
  cin >> n;

  cout << "\nEnter the array:";
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  cout << "\nenter the number to be deleted: ";
  cin >> x;

  cout << endl;

  Delete (arr, n, x);

  return 0;
}


//inserting and element in an array
using namespace std;

int *
insert (int arr[], int n, int x, int position)
{

  int i;
  n = n + 1;

  for (i = n; i >= position; i--)
    {
      arr[i] = arr[i - 1];
    }

  arr[position - 1] = x;

  return arr;
}

int
main ()
{

  int x, position, n;



  cout << "Enter the no of elements: ";
  cin >> n;

  int arr[n];

  cout << "\nEnter the array:";
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  cout << "\nenter the number to be inserted: ";
  cin >> x;

  cout << "\nEnter the position: ";
  cin >> position;
  cout << endl;

  insert (arr, n, x, position);

  for (int i = 0; i < n + 1; i++)
    cout << arr[i] << " ";


  return 0;
}


//linear search in array
using namespace std;

int
main ()
{
  int n, num, index;
  bool x;

  cout << "Enter the no. of elements: ";
  cin >> n;

  int arr[n];


  cout << "\nEnter the array:";
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  cout << "\nEnter the element: ";
  cin >> num;


  for (int i = 0; i < n; i++)
    {
      if (arr[i] == num)
	{
	  x = 1;
	  index = i;
	}

    }

  if (x == 1)
    {
      cout << "\nThe number is present at " << index << " index";
    }

  else
    {
      cout << "\nnumber not found";
    }


  return 0;
}


//reversing array
using namespace std;

int
main ()
{
  int n;

  cout << "Enter the no of elements: ";
  cin >> n;

  int arr[n];
  int array[n];

  cout << "\nEnter the array:";
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  cout << "\nReversed array is: ";


  for (int i = n - 1, j = 0; i >= 0; i--, j++)
    {
      array[j] = arr[i];
    }


  for (int i = 0; i <= n - 1; i++)
    cout << array[i] << " ";


  return 0;
}

