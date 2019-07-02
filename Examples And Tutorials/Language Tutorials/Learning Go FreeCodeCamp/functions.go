package main

import "fmt"

func sayMessage(msg string) {
	fmt.Println(msg)
}

func sayMessage2(msg string, idx int) {
	fmt.Printf("%s\nThe index is %v\n", msg, idx)
}

// Go provides a concise way to declare functions whose paramters have the same type.
// The paramters in the comma-seperated list is inferred to be of the same type
func sayGreetings(greeting, name string) {
	fmt.Println(greeting, name)
}

// Go also allows us define a function that can have variable number of arguments.
// These types of functions are called varadic function, can have `...` in their argument list
// The waay these arguments are passed is through a slice
func sum(values ...int) int {
	fmt.Printf("%T\n", values)
	result := 0

	for _, v := range values {
		result += v
	}

	return result
}

// Go has something called named return, which is a syntax sugar over declaring the return variable
// Don't use it
func sum2(values ...int) (result int) {
	for _, v := range values {
		result += v
	}
	return
}

// To return multiple values from a function, we just need to list the types of the return values
// Also we need to return the values in the type order mentioned in the return-list
func divide(a, b float64) (float64, error /* A object of error type signifies a error in the function */) {
	if b == 0.0 {
		return 0.0, fmt.Errorf("Can't divide by zero")
	}
	return a / b, nil
}

// Passing function as arguments
func callback(op func(int, int) int, values ...int) int {
	res := 1

	for _, v := range values {
		res = op(res, v)
	}

	return res
}

func main() {
	sayMessage("This is the main function.")
	sayMessage2("This is the main function.", 5)
	sayGreetings("Hello", "sTux")

	fmt.Println(sum(1, 2, 3, 4))
	fmt.Println(sum2(5, 6, 7, 2))

	res, err := divide(10, 5)
	fmt.Println(res, err)
	res, err = divide(5, 0)
	fmt.Println(res, err)

	fmt.Println(callback(func(a, b int) int { return a * b }, 1, 2, 3, 4))
}
