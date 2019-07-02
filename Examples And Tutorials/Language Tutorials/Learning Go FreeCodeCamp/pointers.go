package main

import "fmt"

type vector struct {
	x float64
	y float64
}

func main() {
	// NOTE: Go doesn't allows pointer arithmetic. Although it can be enabled via the "unsafe" package in Go library
	a := 42
	fmt.Println(a)

	// Long form syntax to declare a poiner
	var b *int = &a
	fmt.Printf("%v is at %v\n", *b, b)

	// Go allows us to directly create a struct object using address-of operator
	v := &vector{x: 10, y: -10}
	// Deferencing a struct pointer in Go is as same as dereferncing using a struct object
	fmt.Println(v.x, v.y)

}
