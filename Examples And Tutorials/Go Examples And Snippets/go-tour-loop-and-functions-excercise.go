package main

import "fmt"

// This is basically Netwon-Raphson for f(x): x^2 = <some value>
func Sqrt(value float64, iterations int) float64 {
    res := float64(1.0)

    for ; iterations >= 1; iterations-- {
        res -= ((res * res) - value) / (2 * res)
    }

    return res
}

func main() {
    var value float64
    var iters int

    fmt.Printf("Enter value to find root and number of iterations: ");
    fmt.Scanf("%f %d", &value, &iters)

    fmt.Printf("Approx is: %v\n", Sqrt(value, iters))
}
