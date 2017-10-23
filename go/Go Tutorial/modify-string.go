package main


import "fmt"


func main() {
    var s string = "hello";

    var c = []rune(s);  // Convert s into a array of runes
    c[0] = 'H';

    s2 := string(c);

    fmt.Println(s2);
}
