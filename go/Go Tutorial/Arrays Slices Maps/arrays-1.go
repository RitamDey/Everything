package main


import "fmt"


func main() {
    var arr [10]int

    arr[0] = 42
    arr[1] = 13

    fmt.Println(arr)

    arr2 := [10]int{1, 2, 3}

    fmt.Println(arr2)
}
