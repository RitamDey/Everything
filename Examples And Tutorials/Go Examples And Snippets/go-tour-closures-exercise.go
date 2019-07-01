package main

import "fmt"

func fibonacci() func()int {
    a, b := 0, 1

    fmt.Println(a)
    fmt.Println(b)

    return func() int {
        res := a + b
        a, b = b, res
        return b
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
