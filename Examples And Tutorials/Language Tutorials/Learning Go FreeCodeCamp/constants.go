package main

import (
	"fmt"
	"math"
)

// In Go, keeping the first letter of variable/constant to upper-case, it will be a exported (package-public)
// constants without type acts as literals and camn be used with all the variants of the type
func main() {
	// In Go, constants needs to be set during declaration, setting them results of functions is not allowed or even values of other variables
	//const myConst := math.Sin(math.Pi / 2)  // This will error out
	myConst := math.Pi / 2
	fmt.Println("Math operations are in radians", math.Sin(myConst))
}
