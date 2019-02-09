import codecs
from re import findall

# The database was a large JSON which was first Base64 encoded, then hex encoded.
# After that the encoded data was split in line of length 60.
hex_decoder = codecs.getdecoder('hex_codec')
base64_decoder = codecs.getdecoder('base64')


contents = ""
with open('users_db') as fin:
	for i in fin:
		contents += i.strip()

hex_decoded = hex_decoder(contents)[0].strip()
base64_decoded = base64_decoder(hex_decoded)[0].decode()  # Important cause decoders in Python 3 returns a bytes object and Regex on strings

print(findall(r'flag{\w+}', base64_decoded)[0])

