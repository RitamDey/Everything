data class Person(val name: String, val age : Int)


fun getPeople(): List<People> {
    return listOf(Person("Alice", 29), Person("Bob", 31))
}
