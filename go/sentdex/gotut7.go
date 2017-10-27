package main


import "fmt"


const usixteenbitmax float64 = 65535
const kmh_multiple float64 = 1.60934


type car struct {
    gas_pedal uint16
    brake_pedal uint16
    streering_wheel int16
    top_speed float64
}


func (c car) kmh() float64 {
    return float64(c.gas_pedal) * (c.top_speed/usixteenbitmax)
}


func (c car) mph() float64 {
    return float64(c.gas_pedal) * (c.top_speed/usixteenbitmax/kmh_multiple)
}


func (c *car) new_top_speed(newspeed float64) {
    c.top_speed = newspeed
}


func main() {
    a_car := car {gas_pedal: 65000,
                  brake_pedal: 0,
                  streering_wheel: 12561,
                  top_speed: 255.0}

    fmt.Println(a_car)
    fmt.Println(a_car.kmh())
    fmt.Println(a_car.mph())

    a_car.new_top_speed(500)
    fmt.Println(a_car)

    fmt.Println(a_car.kmh())
    fmt.Println(a_car.mph())
}
