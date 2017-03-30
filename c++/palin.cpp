#include<iostream>

using namespace std;

int palin(int);

int main()
{
  int cases,num;
  cin>>cases;
  for(int a=1;a<=cases;a++)
    {
      cin>>num;
      for(int b=num+1;b>0;b++)
	{
	  if(palin(b))
	    {
	      cout<<b<<endl;
	      break;
	    }
	}
    }
  return 0;
}

int palin(int n)
{
  int s=n,rev=0;
  while(n)
    {
      int x=n%10;
      rev=rev*10+x;
      n/=10;
    }
  if(rev==s)
    return 1;
  else
    return 0;
}
