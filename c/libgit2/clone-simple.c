#include <git2.h>
#include <stdio.h>


typedef enum {
    false, true
} bool;


int main(int argc, char **argv){
    git_repository *repo = NULL;  // Pointer to the cloned repo
    const char *url = "http://gitlab.com/GreenJoey/My-Simple-Programs.git";  // The repourl
    const char *repo_path = "/tmp/repo";  // Path of the cloned repo

    int error = git_clone(&repo, url, repo_path, NULL);  // Main clone function

    printf("%d\n", error);
    return 0;
}