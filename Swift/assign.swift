let num1:Int = 100 //Declares a constant binding
var num2:Double = 12.5 //Declares a variable binding

print(num1, num2)
print(Int(num2)) //Explict conversation


var tuple: (Int, Int) = (5, 6) //Tuple type
print(tuple.0) //Acess is done using the '.' operator

var tupleNamed: (x:Int, y:Double, z:String) = (17, 55.55, "Hello World") //Tuples with named positions just like Python's collections.namedtuples
print(tupleNamed.z) //Access is just like tuples but here values are retrived using the position names

var (x, y, name) = tupleNamed //Tuple unpacking and _ works just like in Python
print(x, y, name)
