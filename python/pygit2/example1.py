import  pygit2

# Initializing a bare git repo: git init --bare
pygit2.init_repository('sample', bare=True)

# Initializing a normal git repo: git init
pygit2.init_repository('sample',  bare=False)


# Getting the head commit: git log -1
repo = pygit2.Repository(path='C:/Users/sTux/Codes/')

commit = repo[repo.head.target]
print(commit.message)