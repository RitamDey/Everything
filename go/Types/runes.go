package main


import "fmt"


func main() {
    // Runes is alias int32. It's a UTF-8 encoded code point.
    var x rune = 'H';

    fmt.Printf("%T %v\n", x, x);
}
