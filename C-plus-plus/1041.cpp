#include<iostream>

using namespace std;

int main()
{
 float x,y;
 cin>>x>>y;
 if((y==0)&&(x==0))
  cout<<"Origem\n";
 else if(x==0)
  cout<<"Eixo Y\n";
 else if(y==0)
  cout<<"Eixo X\n";
 else if(y<0)
 {
  if(x>0)
   cout<<"Q4\n";
  else
   cout<<"Q3\n";
  }
 else if(y>0)
 {
  if(x>0)
   cout<<"Q1\n";
  else
   cout<<"Q2\n";
  }
  return 0;
}
