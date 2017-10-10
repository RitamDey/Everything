package main


import "fmt"


func main() {
    /**
     * The keyword range can be used for loops.
     * It can loop over slices, arrays, strings, maps and channels.
     * range is an iterator that, when called, returns the next key-value
     * pair from the "thing" it loops over.
     * Depending on what that is, range returns different things.

     * When looping over a slice or array, range returns the index
     * in the slice as the key and value belonging to that index.
     * Consider this code:
    **/

    list := []string{ "a", "b", "c", "d", "e", "f" }

    for index, value := range list {
        fmt.Printf("Index %v has Value %v\n", index, value)
    }
}
