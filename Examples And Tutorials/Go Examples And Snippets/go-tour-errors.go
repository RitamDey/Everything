package main

import (
    "fmt"
    "time"
)

// Go expresses error with `error` interface values. They are built-in interface similar to `fmt.Stringer`
/**
    type error interface {
        Error() string
    }
**/
// Function returns a value of `error` type, and the calling code should handle them
type MyError struct {
    When time.Time
    What string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("at %v, %s", e.When, e.What)
}

func run() error {
    return &MyError {
        time.Now(),
        "it didn't work",
    }
}

func main() {
    if err := run(); err != nil {
        fmt.Println("Error", err)
    }
}
