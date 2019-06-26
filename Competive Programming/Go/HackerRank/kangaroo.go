package main

import "fmt"

func main() {
    var x1 int
    var x2 int
    var v1 int
    var v2 int

    fmt.Scanf("%d %d %d %d", &x1, &v1, &x2, &v2)

    if solve(x1, x2, v1, v2) {
        fmt.Println("YES")
    } else {
        fmt.Println("NO")
    }
}

func solve(x1 int, x2 int, v1 int, v2 int) bool {
    if v1 == v2 {
        return false
    }

    if x1 > x2 && v1 > v2 {
        return false
    }

    if x2 > x1 && v2 > v1 {
        return false
    }

    return (x1 - x2) % (v1 - v2) == 0
}



