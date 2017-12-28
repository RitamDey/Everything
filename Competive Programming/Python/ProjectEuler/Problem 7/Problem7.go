package main


import "fmt"


func is_prime(n uint64) bool {
    var i uint64;
    if n == 1 {
        return false;
    }

    if n==2 || n==3 {
        return true;
    }

    for i = 2; i <= n/uint64(2); i += 1 {
        if n%i == 0 {
            return false;
        }
    }
    return true;
}


func main() {
    count := 1
    num := uint64(0)

    for ;count<=10001; {
        num += 1
        if is_prime(num) {
            count += 1
        }
    }

    fmt.Println(num);
}
