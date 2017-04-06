#include <curl.h>
#include <stdio.h>


int main(){
    curl_global_init(CURL_GLOBAL_ALL);  //Initialize the libcurl
    
    curl_global_cleanup();  // Destroy libcurl objects
}
