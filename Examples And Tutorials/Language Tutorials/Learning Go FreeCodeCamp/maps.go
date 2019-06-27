package main

import "fmt"

func main() {
	// The declaration of map object is: map[<key type>]<value type>
	// The constrant for keys is that the key type must be tested for equality

	statePopulationUS := map[string]int{
		"Calfornia":    39250017,
		"Texas":        27862596,
		"Florida":      20612439,
		"New York":     19745289,
		"Pennsylvania": 12802503,
		"Illinios":     12801539,
		"Ohio":         11614373,
	}

	fmt.Println(statePopulationUS)

	// Another way to create a empty map is
	population2 := make(map[string]int)
	fmt.Println(population2)

	// Referncing a value in map
	fmt.Printf("Population of Ohio %v\n", statePopulationUS["Ohio"])

	// Putting a value in map
	statePopulationUS["Georgia"] = 10310371
	fmt.Println(statePopulationUS)

	// Deleting a entry from the map
	delete(statePopulationUS, "Georgia")
	fmt.Println(statePopulationUS)

	// Querying for absent key in map, returns the default value of the value type.
	fmt.Println(statePopulationUS["Georgia"])

	// In Go, querying a key in map returns not only the value of key, but also if the key was found in the map or not
	value, present := statePopulationUS["Georgia"] // The value of `present` represents if the key was found in the map or not
	fmt.Println(value, present)
}
