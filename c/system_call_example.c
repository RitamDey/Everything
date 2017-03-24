#include<stdio.h>

int main(){
	system("ls -l");
	system("bash -c 'echo $(uname -a)'");
	return 0;
}
