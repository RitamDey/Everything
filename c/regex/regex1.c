#include <stdio.h>
#include <stdlib.h>
#include <regex.h>


int main() {
    regex_t regex;
    int regex_return;
    char regex_message[1000];
    
    regex_return = regcomp(&regex, "^a[[:alnum:]]" ,REG_ICASE);
    if(regex_return){
        fprintf(stderr, "Can't compile regex\n", NULL, 0);
    }
    
    regex_return = regexec(&regex, "abcABC", 0, NULL, 0);
    
    if(regex_return == 0) {
        puts("Matched");
    }
    else if(regex_return == REG_NOMATCH) {
        puts("No Match");
    }
    else {
        regerror(regex_return, &regex, regex_message, sizeof(regex_message));
        fprintf(stderr, "Regex match failed: %s\n", regex_message);
        exit(regex_return);
    }
    regfree(&regex);
    return 0;
}
