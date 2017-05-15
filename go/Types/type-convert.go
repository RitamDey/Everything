/**
 * Go's type conversion is totally like Python's type coversion
 * To convert a type from type x to type y then;
 * y(x) is used 
**/


package main


import (
        "fmt"
        "math"
    )


func main() {
    var x, y int = 3, 4
    f := math.Sqrt(float64(x*x + y*y))  // math.Sqrt returns a float64 when input is float64
    var z uint = uint(f)
    fmt.Println(x, y, z)
}
