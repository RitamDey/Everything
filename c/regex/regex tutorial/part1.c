#include <stdio.h>
#include <regex.h>
#include <string.h>


int main() {
    regex_t regex;
    int status;
    char regex_pattern[81], test_string[81];

    // Read the regex pattern from the user
    printf("Please give the regex expression: ");
    fgets(regex_pattern, 80, stdin); 
    regex_pattern[strlen(regex_pattern)-1] = '\0';

    // Compile the extended regex
    status = regcomp(&regex, regex_pattern, REG_EXTENDED|REG_NOSUB);
    printf("Validity of regex: %d\n", status);

    if(status)
        // Return if regex compilation fails
        return 1;
    
    while(1) {
        printf("Please give the test string: ");
        fgets(test_string, 80, stdin);
        test_string[strlen(test_string)-1] = '\0';

        if(strlen(test_string) < 1)
            break;
        
        // Execute the regex match on the passed string
        status = regexec(&regex, test_string, (size_t)0, NULL, 0);
        printf("Matched %d\n", status);
    }

    return 0;
}