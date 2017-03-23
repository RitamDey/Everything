#include <stdio.h>
#include <string.h>
int main(){
   char name[] = "Hello World";
   FILE *fout = open("xyz.txt", "w+");
   fwrite(name, sizeof(char), strlen(name), fout);
   fclose(fout);
}
