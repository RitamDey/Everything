import pygit2 as git


repo = git.Repository("/stux/Codes/AlgoDS")
commit = repo[repo.head.target]
print(commit.message)
