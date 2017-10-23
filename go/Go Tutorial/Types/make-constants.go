package main


import "fmt"


func main() {
    const (
        world = "Hello World"
        python = "Rules!"
        ruby = "Can rule!"
        golang = "will rule Someday!"
    )

    fmt.Println(world)

    fmt.Printf("Python %s\nRuby %s\nGo %s\n", python, ruby, golang)
}
