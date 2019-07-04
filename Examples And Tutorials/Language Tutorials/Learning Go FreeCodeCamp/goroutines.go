package main

import (
	"fmt"
	"runtime"
	"sync"
)

// WaitGroup are used to sync the execution of Go routines on green threads
var wg = sync.WaitGroup{}
var rw = sync.RWMutex{}
var counter = 0

func sayHello() {
	fmt.Printf("Hello from %v\n", counter)
	wg.Done() // This signals the wait group that a task has finished and to decrement the waiting counter
}

func increment() {
	counter++
	wg.Done()
}
func main() {
	// Maximum number of go routines allowed. A value of -1 returns the current value of allowed proc
	runtime.GOMAXPROCS(100)
	wg.Add(1) // This add the number of tasks of tasks that are waiting on the wait group
	// Creates a lightweight green thread for the function
	go sayHello()

	wg.Wait() // This makes the main thread wait until all the tasks in the wait group has finished executing

	for i := 0; i < 10; i++ {
		wg.Add(2)
		rw.RLock()
		go sayHello()
		rw.RUnlock() // Unlocks the mutex held for reading
		rw.Lock()
		go increment()
		rw.Unlock() // Unlocks the mutex held for writing
	}

	wg.Wait()
}
