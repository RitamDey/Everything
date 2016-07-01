#include<iostream>

using namespace std;

int main()
{
  int cases;
  cin>>cases;
  for(int a=1;a<=cases;a++)
    {
      unsigned long int num;
      cin>>num;
      if(num==0)
	cout<<"NULL"<<endl;
      else if(num%2==0)
	{
	  cout<<"EVEN ";
	  if(num<0)
	    cout<<"POSITIVE"<<endl;
	  else
	    cout<<"NEGATIVE"<<endl;
	}
      else
	{
	  cout<<"ODD ";
	  if(num<0)
	    cout<<"POSITIVE"<<endl;
	  else
	    cout<<"NEGATIVE"<<endl;
	}
    }
  return 0;
}
