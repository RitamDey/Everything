package main

import (
	"fmt"
)

func main() {
	a := 10
	b := 3
	f1 := 10.2
	f2 := 3.7
	c1 := 1 + 2i
	c2 := 2 + 5.2i

	fmt.Println("=====================================\nArithmetic Ops")
	fmt.Println(a+b, f1+f2, c1+c2)
	fmt.Println(a-b, f1-f2, c1-c2)
	fmt.Println(a*b, f1*f2, c1*c2)
	fmt.Println(a/b, f1/f2, c1/c2) // Go won't change types even if result is float
	fmt.Println(a%b, "Modulus with floats and complex doesn't makes sense, neither does binary ops")
	fmt.Println("=====================================")

	// Go won't errors out if the types of the operands mismatch.
	// It won't type until explictly asked so
	var c int16 = 10
	var d int8 = 3
	// fmt.Println(c * d)  //This code errors with mismatched types
	fmt.Println(c * int16(d)) // This won't because of explict conversion

	fmt.Println("=====================================\nBinary Ops")
	fmt.Println(a & b)
	fmt.Println(a | b)
	fmt.Println(a ^ b)
	fmt.Println(a &^ b) // 1010 &^ 0011 = 0100
	fmt.Println("=====================================")

	fmt.Println("=====================================\nBitshift Ops")
	fmt.Println(a << 3)
	fmt.Println(a >> 3)
	fmt.Println("=====================================")
}
