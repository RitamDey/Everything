package main


import (
    "fmt"
    "math"
    "math/rand"
)


func foo() {
    // In Go, functions and propeties starting with capital is only visible
    fmt.Println("The square root of 4 is", math.Sqrt(4))
}


func main() {
    foo()
    fmt.Println("A random number coming up", rand.Intn(100))
}
