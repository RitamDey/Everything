fun main() {
    // val keyword is used for declaration of constant values
    val name: String = "Ritam"

    // var keyword is used for declaration of variable values
    var last: String
    last = "Dey"

    // To have a variable have null value, a `?` is required which makes it nullable type
    // Types are "non-null" by default in Kotlin
    var greeting: String? = null
    greeting = "Hello "

    if (greeting == null)
        println(name + " " + last);
    else
        println(greeting + name + " " + last);

    // when statment is Kotlin's answer to switch statment in Java
    when (greeting) {
        null -> println(name + " " last);
        else -> println(greeting + name + " " + last);
    }
}
