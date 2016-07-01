#include<iostream>

using namespace std;

int main()
{
string s;
char last;
int cases;
cin>>cases;
for(int a=1;a<=cases;a++)
{
cin>>s;
//last=s[0];
//cout<<last;
for(int p=0;p<s.size();p++)
{
if(s[p]!=s[p+1])
cout<<s[p];
last=s[p];
}
cout<<endl;
}
return 0;
}
