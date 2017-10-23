package main


import (
        "fmt"
        "math"
    )


func main() {
    // To have string C like string formatter, We need to use Printf method.
    fmt.Printf("I have %.10f problems\n", math.Sqrt(9))
    fmt.Printf("%f\n", math.Sqrt(7))
}
