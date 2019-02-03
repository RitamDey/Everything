# Doesn't work completely

decode_table = {
	"aaaaa": 'A',
	"aaaab": 'B',
	"aaaba": 'C',
	"aaabb": 'D',
	"aabaa": 'E',
	"aabab": 'F',
	"aabba": 'G',
	"aabbb": 'H',
	"abaaa": "I",
	"abaab": "K",
	"ababa": 'L',
	"ababb": 'M',
	"abbaa": 'N',	
	"abbab": 'O',
	"abbba": 'P',
	"abbbb": 'Q',
	"baaaa": 'R',
	"baaab": 'S',
	"baaba": 'T',
	"baabb": 'U',
	"babaa": 'W',
	"babab": 'X',
	"babba": 'Y',
	"babbb": 'Z'
}


def decipher(cipher):
	decipher_text = ""
	chunk = ""
	i = 0
	while i < len(cipher):
		if len(chunk) < 5:
			chunk += cipher[i]
			i += 1
		else:
			print(decode_table[chunk.lower()])
			decipher_text += decode_table[chunk.lower()]
			chunk = ""

	return decipher_text


if __name__ == '__main__':
	cipher_text = input().strip()
	print(decipher(cipher_text))
