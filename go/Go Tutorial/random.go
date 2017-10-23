package main


import (
        "fmt"
        "math/rand"  // math/rand will import only the rand from the math packages
    )


func main() {
    fmt.Println("My seed ", rand.Seed)

    /**
    The rand's Intn method requires a number for the random to be genrated
    Alo the number returned is same. This has to do something with machine's seed
    **/
    fmt.Println(rand.Intn(10), rand.Intn(100))
}
