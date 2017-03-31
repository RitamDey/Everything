import pygit2


# Showing a git commit: git show <commit id>

repo =  pygit2.Repository('C:/Users/sTux/Codes/')

# Parses a single revision
commit = repo.revparse_single('8cda658174fa6d4c060976986a47b5d4018841a9')


# Gets the message of the commit an its hex and its diff
message = commit.message
commit_hex = commit.hex
diff = repo.diff(commit.parents[0], commit)
print(diff)
# files = []
# for e in commit.tree:
#     print(e.name)
