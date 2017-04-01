#include <git2.h>
#include <stdio.h>


typedef enum bool {
    false,  true
} bool;

int main(int argc, char **argv){
    git_libgit2_init();  // Initializing the libgit2 global state
    int error;  // Storage for errors

    git_repository *repo = NULL; 

    error = git_repository_init(&repo, "/tmp/git1", false);  // Normal git repo

    error = git_repository_init(&repo, "/tmp/git2", true);  // Bare git repo
    git_libgit2_shutdown();  // Shutdown the libgit2 states
}
