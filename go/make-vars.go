package main


import "fmt"


var c, python, java bool  // These are called package level variables


func main() {
    var i int  // These are called function level variables
    fmt.Println(i, c, python, java)
}
