class Greet{
 def name
 Greet(who){name=who[0].toUpperCase()+who[1..-1]}
 def salute(){println "Hello $name!"}
}
g=new Greet("World")
g.salute()
