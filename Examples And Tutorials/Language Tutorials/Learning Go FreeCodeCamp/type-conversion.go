package main

import (
	"fmt"
	"strconv"
)


func main() {
	var i int = 42;

	// To convert int to float, we can do it as
	var j float32
	j = float32(i)

	// Also Go doesn't allow implict conversion of types, so that it doesn't loose imformation on conversion
	// This line of code will create a error
	// j = i	

	fmt.Printf("%T %v\n", i, i)
	fmt.Printf("%T %v\n", j, j)

	var k string
	k = string(i)

	// Go works with Unicode characters. The conversion above will result in Go using the value of i for the Unicode character
	fmt.Println(k)

	// The correct way of converting ints to string is using strconv package
	k = strconv.Itoa(i)  // Itoa -> Integer to ASCII
	fmt.Println(k)
}