package main

import (
        "fmt"
        "math"
    )


func sqrt(x float64) string {
    if x < 0 {
        return sqrt(-x) + "i"
    }
    return fmt.Sprint(math.Sqrt(x))
}


func main() {
    fmt.Printf("Sqrt of 2 %v\nSqrt of -4 %v\n", sqrt(2), sqrt(-4))
}
