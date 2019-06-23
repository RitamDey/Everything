package main

import "fmt"

// For the module scope,
// Any variable with lowercase is scoped as package private
// While any variable with uppercase is scoped as package public

// Declaring variables in the package level needs the explict syntax
var name string = "sTux"

func main() {
    fmt.Println("Hello Go!")
    
    // Declaring and initializing variables in Go with explict types mentioned
    var i int
    i = 42
    fmt.Println(i)

    i = 27
    fmt.Println(i)

    // Go can also infer the type of variable from the value it is declared with
    j := "45"
    fmt.Printf("%v %T\n", j, j)  // The %v format in Go is to print the value and the %T is used to print the type of the variable

    fmt.Printf("%T %v\n", name, name)

    // This won't run since re-declaring of variables in same scope is not allowed in Go
    // i := 55

    // This is a declaration block in Go. It is used to declare related variables all in a single space
    var (
        name string = "Ritam"  // Shadows module scope
        age int = 20
    )

    fmt.Printf("Name %v Age %v\n", name, age)

    // Go compile time errors if a variable is declared and not used.
    // The following code will cause error
    // z := "Hello World"

    
}