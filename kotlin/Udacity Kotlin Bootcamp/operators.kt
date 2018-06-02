fun main(args: Array<String>) {
    val fish = 2  // Kotlin keeps numbers as primitives

    // But calling methods on them is allowed
    println(fish.times(6))
    println(fish.div(6))
    println(fish.plus(6))
    println(fish.minus(6))

    //use primitive `int` as an object
    println(1.toLong())

    // or, put `int` in a box
    val boxed: Number = 1
    println(boxed.toLong())

    val constant = 1  // We declare constants using `val`
    var variable = 2  // We decalare variables using `var`
    variable = 3

    // Kotlin allows `_` to be used a group seperators
    val oneMillion = 1_000_000
    val socialSecurity = 999_99_9999L
    val hex = 0xFF_EC_DE_5E
    val bytes = 0b10111_00111_101100_00011


    val byte : Byte = 1
    val j: Int = byte.toInt()  // Normal process
    /*
    val i: Int = byte  // Disallowd by Kotlin for safety
    */

    // Nullibity in Kotlin

    // Variables declared explictly can't be null
    // val rocks: Int = null  // Will give errors
    var marbles: Int? = null  // Process of saying if a variable can be null

    // Can have null elements
    var lotsOfFish: List<String?> = listOf(null, null)
    
    // Can hold a null value but not null elements
    var evenMoreFish: List<String>? = null

    // Also the varibale can be List which may contain null
    // elements or even may have null value itself
    var otherFish: List<String?>? = null
    otherFish = listOf("Goldy", null)

    println(otherFish)

    // Check if `fish` is null and call the method or use the other value
    println(fish?.dec() ?: 0)

    val fish2: Int? = null
    println(fish2?.dec() ?: 0)

    // The `!!` operator bypasses all the nullity tests
    println(fish2!!.dec())
}