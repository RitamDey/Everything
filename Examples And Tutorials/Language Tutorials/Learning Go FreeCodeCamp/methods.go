package main

import (
	"fmt"
	"math"
)

type vertex struct {
	X float64
	Y float64
}

// A method in Go is a method if it has a associated type added to it, called "Known context".
// To associate a type with a function,  we just need to put a (<object name> <type>) between the func keyword and the function name
// This object would be avaliable to the function
//    ~~~~~~~~~ -> Is called a value reciver and recieves a copy of the value of the object. This doesn't actually modify the object we have passed
func (v vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

//   ~~~~~~~~~~~ -> Is called a pointer reciver and recieves a pointer to the object we are working with. This can modify the object itself.
func (v *vertex) Add(other vertex) {
	v.X += other.X
	v.Y += other.Y

	return
}
func main() {
	v := vertex{X: 3, Y: 4}
	fmt.Println(v.Abs())
	v.Add(vertex{5, 4})
	fmt.Println(v)
}
