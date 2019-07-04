package main

import "fmt"

type ErrNegetiveSqrt float64

func (err ErrNegetiveSqrt) Error() string {
    // Can't directly use fmt.Sprintf("%v", err) would call err.Error() to convert err to string, which causes a infinite recursion
    rep := fmt.Sprintf("%v", float64(err))
    return fmt.Sprintf("cannot Sqrt negative number:%v", rep)
}

func Sqrt(x float64) (float64, error) {
    res := 1.0

    if x < 0 {
        return x, ErrNegetiveSqrt(-2)
    }

    for iters := 1; iters <= 100; iters++ {
        res -= ((res * res) - x) / (2 * res)
    }

    return res, nil
}

func main() {
    fmt.Println(Sqrt(-2))
    fmt.Println(Sqrt(2))
}
