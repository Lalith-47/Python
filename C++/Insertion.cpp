#include <iostream>
#include <conio.h>
using namespace std;
int main()
{
    int a[10], i, n, j, k, value;
    cout << "Enter number of elements to be entered: ";
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << "Enter at what location do you want to insert the new value: ";
    cin >> k;
    cout << "Enter the value: ";
    cin >> value;
    // Insertion part
    i = n;
    while (i != k)
    {
        a[i] = a[i - 1];

        i--;
    }
    a[k] = value;
    for (i = 0; i <= n; i++)
    {
        cout << a[i] << ' ';
    }
}