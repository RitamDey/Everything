package main

import "fmt"

func main() {
	// There are 2 initlializer syntax for arrays in Go

	// This one is used when we are setting the values of arrays during declaration
	grades := [...]int{97, 85, 93}
	fmt.Printf("Grades: %v %T\n", grades, grades)

	// This one is used when we just want a array with fixed length and all the elements initialized to default
	var arr2 [3]string
	arr2[0] = "Ritam"

	// The len() is used to find length of arrays and array-like data types
	fmt.Println(arr2, len(arr2))

	// Declaring multi-dimensional matrix in Go
	identityMatrix := [...][3]int{[...]int{1, 0, 0}, [...]int{0, 1, 0}, [...]int{0, 0, 1}}
	fmt.Println(identityMatrix)

	// In Go, arrays are treated as values by default and coping them, will copy the entire array instead of copying a pointer to the array
	x := [...]int{1, 2, 3}
	y := x
	y[1] = 741852963
	fmt.Println(x, y)

	// Slices in Go are more like arrays in Python. They can grow dynamically as we add data.
	// Most operations of arrays can also be done in slices
	// Declaration syntaxes
	a := []int{1, 2, 3} // Array-like

	// From array
	arr1 := [...]int{7, 4, 1, 8, 5, 2, 9, 6, 3}
	s1 := arr1[:]   // slice of all elemets
	s2 := arr1[3:]  // From 4th
	s3 := arr1[:6]  // Till 5th
	s4 := arr1[3:6] // From 4th till 5th
	fmt.Println(arr1, s1, s2, s3, s4)

	// Using make function
	s5 := make([]int, 3) // Creates a slice of capacity and length 3
	fmt.Printf("Slice: %v Length: %v Capacity: %v\n", s5, len(s5), cap(s5))
	s6 := make([]int, 3, 10) // Creates a slice of length 3 and capacity 10
	fmt.Printf("Slice: %v Length: %v Capacity: %v\n", s6, len(s6), cap(s6))

	fmt.Printf("%v %T\n", a, a)
	// len() is same, cap() returns the capacity of the underlying backing array
	fmt.Println(len(a), cap(a))

	// Slices are a real referntial type
	b := a
	b[1] = 963852741
	fmt.Println(b, a)

	// Appending elements to a slice
	s6 = append(s6, 123456789) // append() can take any number of arguments, every arg after first is elements to append
	fmt.Println(s6)

	// Appending a slice to another is done using the `...` operator, which is same as `*` operator in Python
	s7 := []int{123, 456, 789}
	s6 = append(s6, s7...)
	fmt.Println(s6)

	// Popping elements from slice
	// elem := re
}
