from mutagen.id3 import ID3
from sys import argv


audio = ID3(argv[1])

print(f"Title is {audio.get('TALB').pprint()}")
