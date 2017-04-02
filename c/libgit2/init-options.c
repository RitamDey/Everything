#include <git2.h>
#include <stdio.h>


typedef enum bool {
    false, true
} bool;


int main(){
    int error;
    git_repository *repo = NULL;  // Pointer to the repo
    git_repository_init_options opts = GIT_REPOSITORY_INIT_OPTIONS_INIT;  // Options for the repo

    /*
     * Customizing the flags
     */

    opts.flags |= GIT_REPOSITORY_INIT_MKPATH;  /// mkdir as needed to create repo
    opts.description = "My repository";

    error = git_repository_init_ext(&repo, "repo/", &opts);

    return 0;
}
