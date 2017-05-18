/**
 A defer statement defers the execution of a function until the surrounding function returns.
The deferred call's arguments are evaluated immediately, 
But the function call is not executed until the surrounding function returns. 
**/

package main


func main() {
	defer println("World")  // This will execute after all the function calls in main() has finished

	print("Hello ")
}