package main

import "fmt"

type I interface {
    M()
}

type T struct {
    S string
}

func (t *T) M() {
    // Handle if the the recived object is <nil>
    if t == nil {
        fmt.Println("<nil>")
        return
    }
    fmt.Println(t.S)
}

func describe(i I) {
    fmt.Printf("(%v, %T)\n", i, i)
}

func main() {
    var i I
    var t *T

    i = t
    describe(i)

    // Calling a method on nil interface is perfectly fine, since the handling of nil is delegated to the method
    i.M()

    i = &T {S: "hello"}
    describe(i)
    i.M()

    // But calling a interface method on a object with no value or concrete type is a error in Go. The following code doesn't works
    /**
    var i I
    describe(i)
    i.M()
    **/
}
