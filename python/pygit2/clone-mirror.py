import pygit2


def mirror(repo, name, url):
    # Create the remote with a mirroring url
    remote = repo.remotes.create(name, url, "refs/*:refs/*")

    # And set the config option to true for the push command
    mirror_var = "remote.{}.mirror".format(name)
    repo.config[mirror_var] = True

    # Return the remote, which pyhit2 will use to perform th clone
    return remote


print("Cloning pygit2 as mirror")
pygit2.clone_repository("https://github.com/libgit2/pygit2", "pygit2.git",
                        bare=True, remote=mirror)

