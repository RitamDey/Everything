package main

import "fmt"

func main() {
  fmt.Print("Enter temperatue in Fahrenheit ")
  var f float32
  fmt.Scanf("%f",&f)
  fmt.Println("The Celsius eq is ",((f-32)*5)/9)
}
