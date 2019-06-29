package main

import (
	"fmt"
	"math"
)

func main() {
	// Simplest form of `if`
	// In Go, there is no braces around conditions and {} are mandatory
	if true {
		fmt.Println("Simplest if statment")
	}

	// The initializer syntax of `if`
	statePopulationUS := map[string]int{
		"Calfornia":    39250017,
		"Texas":        27862596,
		"Florida":      20612439,
		"New York":     19745289,
		"Pennsylvania": 12802503,
		"Illinios":     12801539,
		"Ohio":         11614373,
	}

	// This syntax allows a declaration statment to preeced the actual condition.
	// Here the declaration of pop and ok preeced the condition
	if pop, ok := statePopulationUS["Florida"]; ok {
		fmt.Println(pop)
	}
	// The conditionals are
	/** if { ....
	} else if { ....
	} else { ....
	}
	**/

	// This block of code print Diffrent because of the floating point precision error
	myNum := 0.123
	if myNum == math.Pow(math.Sqrt(myNum), 2) {
		fmt.Println("All the same")
	} else {
		fmt.Println("Diffrent")
	}

	// Trivial switch case example
	switch 2 {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	default:
		fmt.Println("noice")
	}

	// In Go, cases can have mutiple tags and switch can have initializer syntax-ed check
	switch i := 2 + 3; i {
	case 1, 5, 10:
		fmt.Println("odds")
	case 2, 4, 6:
		fmt.Println("evens")
	default:
		fmt.Println("nopa")
	}

	// Go also allows expression to be the tags for case.
	// In this form, the switch does not have a label but all the case does, which are expressions
	// And also in this Go allows the cases to overlap, and in such case the fist satisfying case is executed
	i := 10
	switch {
	case i <= 10:
		fmt.Println("Almost 10")
	case i <= 20:
		fmt.Println("Almost 20")
	default:
		fmt.Println("OUT")
	}

	// Sice Go's default case behaviour is breaking out, if we want to execute all the subsequrnt cases after the succesful one the use keyword `fallthrough`
	switch {
	case i <= 10:
		fmt.Println("Almost 10")
		fallthrough // falls through the case
	case i <= 20:
		fmt.Println("Almost 20") // breaks out as fall through is not indicated
	default:
		fmt.Println("OUT")
	}

	// Go has a special type of switch called Type switching
	// The only requirment is that the value we are using for type switching needs to be a interface
	var k interface{} = 1
	switch k.(type) {
	case int:
		fmt.Println("INT")
	case float64:
		fmt.Println("FLOAT")
	default:
		fmt.Println(i)
	}
}
