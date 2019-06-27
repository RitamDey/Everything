package main

import (
	"fmt"
	"reflect"
)

// The strcts in Go, is similar to C structs
type Doctor struct {
	number int
	// To make the field name of a public struct package-public: the field name also needs to start with upper-case
	ActorName  string // This field is package-public
	companions []string
}

// Go doesn't support inheritance of structs. Instead it supports embedding, where we can embed the fields of one struct into another
type Animal struct {
	// A field can have a tag that reflects the characteristics of the field. They have no functionality of their own but needs a parser to enforce
	Name   string `required max: "100"`
	Origin string
}

// This is the syntax. The `Animal` struct is embedded into `Bird` struct
type Bird struct {
	Animal
	SpeedKPH float32
	CanFly   bool
}

func main() {
	aDoctor := Doctor{
		number:    3,
		ActorName: "Jon Pertwee",
		companions: []string{
			"Liz Shaw",
			"Jo Grant",
			"Sarah Jane Smith",
		},
	}

	fmt.Println(aDoctor)

	// Go allows the declaration of ananomyous structs
	bDoctor := struct{ name string }{name: "John Pertwee"}

	fmt.Println(bDoctor)

	// Sice `Bird` has embedded the struct `Animal`, it inherits all the properties of `Animal`
	b := Bird{}
	b.Name = "Emu"
	b.Origin = "Australia"
	b.SpeedKPH = 48
	b.CanFly = false

	// Or the struct could have been populated like this. Note it needs info about struct's internal layout
	b = Bird{
		Animal: Animal{
			Name:   "Emu",
			Origin: "Australia",
		},
		SpeedKPH: 48,
		CanFly:   false,
	}

	fmt.Println(b)

	// Tags can be found by using Go's reflect package
	t := reflect.TypeOf(Animal{})
	// The FieldByName() returns the field along with a indicator if the field was found in the strcut or not
	field, _ := t.FieldByName("Name")
	fmt.Println(field)
}
