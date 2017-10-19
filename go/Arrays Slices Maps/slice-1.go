package main


import "fmt"


func main() {
    arr := [...]int{1, 2, 3, 4, 5}

    fmt.Printf("arr[2:4]: %v\n", arr[2:4])
    fmt.Printf("arr[1:5]: %v\n", arr[1:5])
    fmt.Printf("arr[:]: %v\n", arr[:])
    fmt.Printf("arr[:4]: %v\n", arr[:4])
    fmt.Printf("arr[1:5][:]: %v\n", arr[1:5][:])
    fmt.Printf("arr[2:4:5]: %v\n", arr[2:4:5])
}
