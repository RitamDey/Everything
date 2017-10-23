package main

import "fmt"

func main() {
	x := 15
	a := &x

	fmt.Printf("%T: %v\n", a, a)
	fmt.Println(*a)

	*a = 5
	fmt.Println(x)

	*a = *a * *a
	fmt.Println(x)
}
