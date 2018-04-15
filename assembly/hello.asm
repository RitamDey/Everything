section .data
    msg db          "Hello World", 10  ; The `10` represents the newline character in Assembly


section .text
    global _start

_start:
    ; The `sys_write` system call has the id of 1 in the syscall table.
    ; It takes 3 arguments
    ; The file-descriptor to where it will write the data
    ; The character string that needs to be written out
    ; The length of the character string to write
    
    mov     rax, 1  ; Store the id of the syscall to rax, here sys_write
    mov     rdi, 1  ; Store the first paramter of the system call, the file-descriptor, here the descriptor of stdout
    mov     rsi, msg  ; Store the second parameter of the system call, the character string, here the value of msg
    mov     rdx, 14  ; Store the third paramter of the system call, the length of the character string, here the length of msg
    syscall  ; Use the syscall instruction to call the OS syscall corresponding to the one in `rax`

    ; The `exit` system call has the id of 60 in the syscall table
    ; It takes only one argument
    ; An integer representing the exit code with which the program shall exit
    mov     rax, 60  ; Store the id of exit syscall to rax
    mov     rdi, 0  ; Store the argument to exit syscall
    syscall  ; Actually call the exit syscall

