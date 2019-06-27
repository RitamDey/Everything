package main

import "fmt"

// `iota` is a special value that can be used when creating enumeratec types.
// The value of `iota` increases by 1 everytime it is used again
const (
	// The const block allows for implict value initialization.
	_  = iota             // ignore the first value, 0
	KB = 1 << (10 * iota) // This formulae will be used to used to initialize all the remaining members in the const block
	MB
	GB
	TB
	PB
	EB
	ZB
	YB
)

func main() {
	fileSize := 4000000000.
	fmt.Printf("%.2fGB", fileSize/GB)
}
