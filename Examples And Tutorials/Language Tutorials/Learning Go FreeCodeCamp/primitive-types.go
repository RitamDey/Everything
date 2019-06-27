package main

import (
	"fmt"
)

// In Go, all the variables have a zero value during declaration.
/**
 * Thus `bool` is gonna have false
 * `int`s is gonna have 0
 * `float`s is gonna have 0.00
 * `string` is gonna have ""
**/
func main() {
	var n bool
	m := true
	fmt.Printf("%v, %T\n%v, %T\n", n, n, m, m)

	/**
	In Go, the default size of `int` is platform dependent.
	Although it is gurannted to be atleast 32 bits

	 * int8 			-128 to 127
	 * int16 			-32,768 to 32,767
	 * int32 			-2,147,483,648 to 2,147,483,647
	 * int64 			-9,223,372,036,854,775,808 to 9,223,372,036,775,807
	Along with this int types, there are the unsigned version of these types.
	Also assigning `uint` with negetive values gives a uint overflow error
	  * uint8			0 to 255
	  * uint16			0 to 65,535
	  * uint32			0 to 4,294,967,295
	**/
	var k uint = 16
	// var k uint = 15 - 16
	fmt.Printf("%v %T\n", k, k)

	// The `byte` data is an alias for the `uint8` type, made avaliable because of common usage
	var a byte = 254
	fmt.Printf("%v %T\n", a, a)

	// Go folows the IEEE 754 standard. Go has two types
	// float32		(+-) 1.18E-38 to (+-) 3.4E38
	// float64		(+-) 2.23E-308 to (+-) 1.8E308
	f1 := 3.14
	// Below are the ways to declare floats using exponent notations
	f2 := 13.7e72
	f3 := 2.1E14
	fmt.Println(f1, f2, f3)

	// Go has complex as primitive types. It has two types
	// `complex64` and `complex128`
	c2 := 2 + 5.2e5i
	fmt.Printf("%v %T\n", c2, c2)
	// To get the real and/or imaginary part, Go has the real() and imag() built-ins
	fmt.Println(real(c2), imag(c2))

	// Go strings are UTF-8 encoded and immutable
	s := "this is string"
	// Go doesn't have character types, but are of type `uint8`
	fmt.Printf("%v %T\n", s, s)
	fmt.Println([]byte(s))

	// Go has `rune` which are UTF-32 encoded strings, which are alias for `int32`
	var r rune = 'i'
	fmt.Printf("%v %T\n", r, r)
}
