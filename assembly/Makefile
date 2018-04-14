all:
	nasm -f elf64 -o $(OUTPUT).o $(OUTPUT).asm
	ld -o $(OUTPUT) $(OUTPUT).o

clean:
	rm -f $(OUTPUT) $(OUTPUT).o
