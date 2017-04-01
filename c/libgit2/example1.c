#include <git2.h>
#include <stdio.h>


int main(){
    git_repository *repo;
    int error = git_repository_open(&repo, "/home/stux/Codes");

    git_object *commit_obj;
    error = git_revparse_single(&commit_obj, repo, "8cda65");
    git_commit *commit = (git_commit *)commit_obj;

    printf("%s", git_commit_message(commit));
    const git_signature *author = git_commit_author(commit);
    printf("%s <%s>\n", author->name, author->email);
    const git_oid *tree_id = git_commit_tree_id(commit);

    git_commit_free(commit);
    git_repository_free(repo);

    return 0;
}
