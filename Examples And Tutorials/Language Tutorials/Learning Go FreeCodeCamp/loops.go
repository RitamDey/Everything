package main

import "fmt"

func main() {
	// Simplest form of for-loop in Go.
	// Also the `++` operator is not a expression but it's a statment on its own
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Go has no "," operator. So to have multiple statments in a for block, we use like this
	for i, j := 0, 0; i < 5; i, j = i+1, j+2 {
		fmt.Println(i, j)
	}

	count := 0

	for {
		if count > 5 {
			break
		}
		fmt.Println("This is how Go does infinite loops")
		count++
	}

	count = 0
	for count < 5 {
		fmt.Println("This is Go's approach to while loops")
		count++
	}

	// Iterating over collections in Go is done using for-range loops.
	// They are basically Go's answer to for-in loops
	s := []int{1, 2, 3}
	for k, v := range s {
		fmt.Println(k, v)
	}

	c := map[int]string{
		1: "sTux",
		2: "Joe",
		3: "BangaliBabu",
	}
	for k, v := range c {
		fmt.Printf("%v -> %v\n", k, v)
	}

	p := "Hello Go"
	for k, v := range p {
		fmt.Println(k, v, string(v))
	}
}
