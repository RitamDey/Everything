package main

import "fmt"


func split(sum int) (x, y int) {
    /**
    * Go's return values may be named. If so, they are treated as variables defined at the top of the function.
    * These names should be used to document the meaning of the return values. 
    * A return statement without arguments returns the named return values. This is known as a "naked" return. 
    * Naked return statements should be used only in short functions, as with the example shown here. They can harm readability in longer functions. 
    **/

    x = sum - 5
    y = sum / 5

    return  // This statment is required to actually return value(s)
}


func main() {
    fmt.Println(split(7))
}
