import  pygit2
import subprocess

# Initializing a bare git repo: git init --bare
pygit2.init_repository('sample', bare=True)

# Initializing a normal git repo: git init
pygit2.init_repository('sample',  bare=False)


subprocess.call('ls')
subprocess.call(['rm', '-r', 'sample'])