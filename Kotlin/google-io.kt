package com.jetbrains.gio


/**
 * A data class basically contains some attribute and getter and setter methods.
 * Also some attributes are `val`, then the attribute doesn't have setters.
**/
data class Money(val amount: Int, val currency: String)


fun main(args: Array<String>) {
    val tickets = Money(100, "$")
    val popcron = tickets.copy(500, "$")

    if(tickets != popcron) {
        println("They are different")
    }
}
