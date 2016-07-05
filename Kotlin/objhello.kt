fun main(args: Array<String>){
 Greeter(args[0]).greet()
}

class Greeter(val name:String){
 fun greet(){
  println("Hello $name")
 }
}
