/*
// Sample code to perform I/O:

cin >> name;                            // Reading input from STDIN
cout << "Hi, " << name << ".\n";        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int n,t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        if(n%2==0)
        {
            cout<<n/2<<endl;
        }
        else
        {
            cout<<(n+1)/2<<endl;
        }
    }
    return 0;
}
