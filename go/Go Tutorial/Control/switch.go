package main


import "runtime"


func main() {
    print("Go runs on ")

    switch os := runtime.GOOS; os {
    case "darwin":
        println("OS X")
    case "linux":
        println("Linux")
    default:
        println("%s", os)
    }
}
