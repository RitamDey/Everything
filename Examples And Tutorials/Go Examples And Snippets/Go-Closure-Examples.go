package main

import "fmt"

func adder() func(int) int {
    /**
    A closure is a function that can reference variables from outside its body. The function may assign and access to the refernced variables; in the sense the closure is "bound" to the variables
    **/
    sum := 0

    return func(x int) int {
        sum += x
        return sum
    }
}

func main() {
    pos, neg := adder(), adder()

    for i := 0; i < 10; i++ {
        fmt.Println(
            pos(i),
            neg(-2*i),
        )
    }
}
