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

    /**
     * You can also use range on strings directly.
     * Then it will break out the individual Unicode characters 6 Mostly,
     * when people talk about characters, they mean 8 bit characters.
     * As UTF-8 characters may be up to 32 bits the word rune is used.
     * In this case the type of char is rune. and their start position,
     * by parsing the UTF-8.
     * The loop:
    **/

    for pos, char := range "Gő!" {
        fmt.Printf("Character '%c' starts at position %d\n", char, pos)
    }
}
