/**
 * The program I am going to describe in this tutorial wants to replicate a
 * very basic version of the git utility command
 *
 * git log --pretty=oneline
 *
 * which lists commit objects in reverse chronological order showing their
 * hash and short commit summary.
 *
 * The original git-log offers tens of different options, but I want to
 * keep things simple here.
**/
#include <git2.h>
#include <stdio.h>
#define REPO_PATH "/stux/Codes/AlgoDS"


int main(int argc, char *argv[]) {
    git_libgit2_init(); // Initialises the necessary resources

    git_repository *repo = NULL;
    git_repository_open(&repo, REPO_PATH);  // Open the repo


    git_revwalk *walker = NULL;
    git_revwalk_new(&walker, repo);  // Creating a git revision walker


    git_revwalk_sorting(walker, GIT_SORT_NONE);  // Set the default commit sort method


    git_revwalk_push_head(walker);  // Set root as the HEAD for traversal


    git_oid oid;
    git_commit *commit = NULL;


    while(!git_revwalk_next(&oid, walker)) {
        git_commit_lookup(&commit, repo, &oid);  // Get the commit object using the oid

        printf("%s ", git_oid_tostr_s(&oid));
        printf("%s\n", git_commit_summary(commit));

        git_commit_free(commit);
    }

    // Free up the resources

    git_revwalk_free(walker);
    git_repository_free(repo);

    git_libgit2_shutdown();

    return 0;
}
