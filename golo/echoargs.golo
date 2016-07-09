
module EchoArgs

function main = |args|{
  foreach arg in args {
    println("-> "+arg)
  }
}
