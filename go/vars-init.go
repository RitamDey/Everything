package main


import "fmt"


func main() {
    // Variables cxan be initialized at declare time
    var python, ruby string = "Hell Yeah\n", "Hmm. Maybe\n"
    // We can also use this dynamic language like syntax
    var golang = true

    fmt.Printf("Python: %sRuby: %s",python,ruby)
    fmt.Println("Go ", golang)
}
