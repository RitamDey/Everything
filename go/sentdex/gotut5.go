package main


import "fmt"


type car struct {
    gas_pedal uint16  // unsigned 16-bit integer
    brake_pedal uint16
    streeing_wheel int16
    top_speed_kmh float64
}


func main() {
    a_car := car{
            gas_pedal: 22341,
            brake_pedal: 0,
            streeing_wheel: 12567,
            top_speed_kmh: 255.0}

    // Another implict way
    a_car = car{22341, 0, 12562, 255.0}

    fmt.Println(a_car.gas_pedal)
}
