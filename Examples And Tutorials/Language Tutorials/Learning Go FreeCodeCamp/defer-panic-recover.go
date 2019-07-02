package main

import "fmt"

func main() {
	// defer works by defering the execution of the function till the end of the caller's body
	// It's mostly used to release resources held by the functions
	fmt.Println("start")
	defer fmt.Println("middle")
	fmt.Println("end")

	// execution of the defered function occurs in Last-In_First-Out order
	defer fmt.Println("first")
	defer fmt.Println("second")
	defer fmt.Println("third")

	// defer will work with the value that was present during the statment was encountered.
	// It will ignore all the subsequent changes of value
	a := "start"
	defer fmt.Println(a)
	a = "end"

	// Go doesn't have traditional exception mechanism. When an error is encountered, the runtime issues a panic that halts the execution of the process
	// This statments issues a panic
	/**
	a, b := 1, 0
	ans := a / b
	fmt.Println(ans)
	**/

	// It may so happen that due to some conditions, we need to halt. Here we can use "panic()" passing a error string
	fmt.Println("start")
	panic("something bad happend")
	fmt.Println("end")
}
