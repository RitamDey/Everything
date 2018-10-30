package main

import (
        "io"
        "fmt"
        "strings"
)


func main() {
    // This method returns a new reader from a string object
    r := strings.NewReader("Hello, Reader!")

    // Create a slice of length 4
    b := make([]byte, 4)

    // Run and infinite for-loop and keep reading from `r`
    for {
        // Readers return the number of byte read and errors if any
        // and writes the same number of bytes in a byte buffer
        // Signature is: func (T) Read(b []byte) (n int, err error)
        n, err := r.Read(b)
        fmt.Printf("n = %v err = %v b = %v\n", n, err, b)

        fmt.Printf("b[:n] = %q\n", b[:n])
        fmt.Printf("b[]   = %q\n", b)

        // EOF in Go is indicated by a `io.EOF` error.
        // If the error is returned, break from the read loop
        if err == io.EOF {
            break
        }
    }
}
