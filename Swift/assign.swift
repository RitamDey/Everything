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

var arr = [Int]() //Declares an array of type Int
arr = [1, 2, 3] //Assigns values to array
print(arr[0]+arr[1]+arr[2]) //Array access is just other lanuages i.e through []

var dict = [Int:Int]() //Declares a dictonary whose keys are of type Int and values of type String
//dict = [1:"Hello", 2:"World"] //Assigns values of the dict with the syntax <key>:<value>
//dict[3] = "!!!!" //Python style key addition is supported
dict = [1:5, 2:10, 3:15]
print(dict[1], dict[2], dict[3]) //Dictonary access is same as Python