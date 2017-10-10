package main


import "fmt"


func main() {
    /**
    * By default break will break out of the immediate loop
    * Using labeled loop, we mention the break statment from
    * which loop it needs to break out.
    **/
    out: for j := 0; j < 5; j++ {
        for i := 0; i < 10; i++ {
            if i > 5 {
                break out
            }
            fmt.Println(i)
        }
    }
}
