import pygit2

# Getting the head commit: git log -1
repo = pygit2.Repository(path='/home/stux/Codes/')

commit = repo[repo.head.target]  # Get the commit head
print(commit.message)


# Traversing the entire commit history: git log

last_commit = repo[repo.head.target]
for commit in repo.walk(last_commit.id, pygit2.GIT_SORT_TIME):
    # print(f'{commit.id} {commit.message}')
    if 'Merge' in commit.message:
        print(commit.message)
