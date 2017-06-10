msg = "The quick brown fox jumps over the lazy dog"


# Seeing if a string is inside another one
$stdout.puts "\"brown\" inside #{msg}?: #{msg.include?("brown")}"

# Getting the size of the string
$stdout.puts "\nLength of #{msg}: msg.size"

# Counting some particular patters inside a string
$stdout.puts "\nVowels: #{msg.count("aeiou")}"
$stdout.puts "\nConsonants: #{msg.count("^aeiou")}"


# Case magics
$stdout.puts "Going to upper case: #{msg.upcase}"
$stdout.puts "Going to lower case: #{msg.downcase}"
$stdout.puts "Swapping case: #{msg.swapcase}"

msg = "          "+msg+"         "
# Stripping spaces
$stdout.puts msg.lstrip
$stdout.puts msg.rstrip
msg = "   "+msg+"   "
$stdout.puts msg.strip
