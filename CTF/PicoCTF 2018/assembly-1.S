.intel_syntax noprefix
.bits 32

.global asm1

asm1:
	push	ebp
	mov	ebp,esp
	cmp	DWORD PTR [ebp+0x8],0xea
	jg	part_a
part_a:
	cmp	DWORD PTR [ebp+0x8],0x6
	jne	part_c
part_c:
	mov	eax,DOWRD PTR [ebp+0x8]
	add	eax,0x3

