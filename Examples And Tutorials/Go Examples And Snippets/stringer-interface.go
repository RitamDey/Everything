package main

import "fmt"

// Stringer is a interface defined in the fmt package. It is defined as
/**
    type Stringer interface {
        String() string
    }
**/
// Implementing this interface allows any type to be described as string.
type Person struct {
    Name string
    Age int
}

func (p Person) String() string {
    return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

type IPAddr [4]byte

func (ip IPAddr) String() string {
    return fmt.Sprintf("%v.%v.%v.%v", ip[0], ip[1], ip[2], ip[3])
}

func main() {
    a := Person {Name: "Ritam Dey", Age: 20}
    b := Person {Name: "BanagliBabu", Age: -1}

    fmt.Println(a, b)

    hosts := map[string]IPAddr {
        "loopback": {127, 0, 0, 1},
        "googleDNS": {8, 8, 8, 8},
        "Cloudfare DNS": {1, 1, 1, 1},
    }

    for name, ip := range hosts {
        fmt.Printf("%v: %v\n", name, ip)
    }
}
