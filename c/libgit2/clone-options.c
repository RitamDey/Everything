#include <git2.h>
#include <stdio.h>


typedef enum {
    false, true
} bool;


typedef struct {
    int pos;
    double per;
} progress_data;


int fetch_progress (const git_transfer_progress *stats, void *payload){
    /**
     * This function is used to fetch progress from the git_clone()
    **/

    progress_data *pd = (progress_data *)payload;

    printf("%d %f\n", pd->pos, pd->per);
}


void checkout_progress(const char *path, size_t cur, size_t tot, void *payload){
    progress_data *pd = (progress_data *)payload;

    printf("%s %u %u\n %d %f\n", path, cur, tot, payload);
}

int main(int argc, char **argv){
    git_repository *repo = NULL;  // Pointer to the repo
    int error;

    progress_data d = {0};
    git_clone_options clone_opts = GIT_CLONE_OPTIONS_INIT;


    clone_opts.checkout_opts.checkout_strategy = GIT_CHECKOUT_SAFE;
    clone_opts.checkout_opts.progress_cb = checkout_progress;
    clone_opts.checkout_opts.progress_payload = &d;
    clone_opts.checkout_opts = ;
    clone_opts.fetch_opts.callbacks.transfer_progress = fetch_progress;
    clone_opts.fetch_opts.callbacks.payload = &d;

    error = git_clone(&repo, "http://gitlab.com/GreenJoey/My-Simple-Programs.git/", "/tmp/repo", &clone_opts);

    printf("%d\n", error);
    return 0;
}
