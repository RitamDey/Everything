# [Defining and Starting a Thread](https://docs.oracle.com/javase/tutorial/essential/concurrency/runthread.html)

Any application that must use threading must provide code for doing so.

The few ways for doing so are:
*   Provide a _Runnable_ implementation
*   Subclass the _java.lang.Thread_

It is recommended to use the _Runnable_ method although the _java.lang.Thread_ method is easier it locks down the class to only be a subclass of _java.lang.Thread_

The _java.lang.Thread_ class defines a number of methods useful for thread management. These include static methods, which provide information about, or affect the status of, the thread invoking the method. The other methods are invoked from other threads involved in managing the thread and Thread object.
