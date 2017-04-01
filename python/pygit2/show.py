from datetime import tzinfo, timedelta, datetime, timezone
import pygit2
from sys import argv


class FixedOffset(tzinfo):
    """
    Fixed offset in minutes east from UTC
    """

    def __init__(self, offset):
        self.__offset = timedelta(minutes = offset)

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return None

    def dst(self, dt):
        return timedelta(0)



repo = pygit2.Repository('/home/stux/Codes')
try:
    commit = repo.revparse_single(argv[1])
except IndexError:
    commit = repo.revparse_single('HEAD')

message = commit.message
hash = commit.hex
diff = repo.diff(commit.parents[0], commit)
files = []

for file in files:
    files.append(file.name)

tz = timezone(timedelta(minutes=commit.author.offset))
dt = datetime.fromtimestamp(float(commit.author.time), tz)
timestr = dt.strftime('%c %z')
msg = '\n'.join(
        [
            f'commit {commit.tree_id.hex}',
            f'Author {commit.author.name} <{commit.author.email}>',
            f'Date {timestr}',
            '',
            commit.message,
            diff.patch
         ]
                )

print(msg)
