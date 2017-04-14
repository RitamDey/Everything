#include <stdio.h>
#include <string.h>
#include <regex.h>


int main() {
    regex_t regex;
    char regex_pattern[] = "([A-Z]{1,2})[0-9][0-9A-Z]? +[0-9][A-Z]{2}";
    int status;
    char string[101];
    
}