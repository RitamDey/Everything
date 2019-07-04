package main

import (
    "fmt"
    "math"
)

type Abser interface {
    Abs() float64
}

type MyFloat float64  // MyFloat is a new type alias to float64

type Vertex struct {
    X, Y float64
}

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

func (v *Vertex) Abs() float64 {
    return math.Sqrt(v.X * v.X + v.Y * v.Y)
}

func main() {
    var a Abser
    f := MyFloat(-math.Sqrt2)
    v := Vertex {X:3, Y:4}

    a = f  // This is okay since MyFloat implements Abser
    a = &v  // This is also okay since *Vertex implements Abser

    // This would fail since v is Vertex, not a *Vertex and it does not implement Abser
    // a = v

    fmt.Println(a.Abs())
}
