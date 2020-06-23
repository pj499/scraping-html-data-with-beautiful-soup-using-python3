#include <iostream>
using namespace std;

int main()
{
    int n,sum=0;
    cin>>n;
    int a[2*n];
    for(int i=0;i<2*n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<2*n;i++)
    {
        for(int j=i+1;j<2*n;j++)
        {
           if(a[i]>a[j])
           {
             int temp=a[i];
             a[i]=a[j];
             a[j]=temp;
           }
        }
    }
   for(int i=0;i<2*n;i=i+2)
   {
       sum=sum+a[i];
   }
   cout<<sum;
return 0;
}
