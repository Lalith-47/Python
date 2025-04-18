#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
    int a[10], i, n, j, k, value;
    system("cls");
    cout << "Enter number of elements to be entered: ";
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << "Enter at what location do you want to delete the value: ";
    cin >> k;
    // Deletion part
    i = k;
    while (i < n)
    {
        a[i] = a[i + 1];

        i++;
    }
    for (i = 0; i < n - 1; i++)
    {
        cout << a[i] << ' ';
    }
}