package main

import (
	"fmt"
)

/**
  * Unsed variables and imports causes errors in Go.
**/

func add(x, y float64) float64 {
	return x + y
}

func multiple(a, b string) (string, string) {
	return a, b
}

func main() {
	var num1 float64 = 5.6
	var num2 float64 = 9.5
	fmt.Println(add(num1, num2))

	var num3, num4 float64 = 5.5, 9.9
	fmt.Println(add(num3, num4))

	num5, num6 := 10.1, 9.9
	fmt.Println(add(num5, num6))

	w1, w2 := "Hey", "there"
	fmt.Println(multiple(w1, w2))
}
