user_name = ARGV.first  # get the first element from the array
prompt = '> '


puts "Hi #{user_name}."
puts "I'd like to ask you a few questions."
puts "Do you like me #{user_name}"
puts prompt
likes = $stdin.gets.chomp  # same as gets.chomp


puts "Where do you live #{user_name}?"
puts prompt
lives = $stdin.gets.chomp


puts "What kind of computer do you have? ", prompt  # a comma for puts is like using it twice
computer = $stdin.gets.chomp

$stdout.puts """
Alright, so you said #{likes} about liking me.
You live in #{lives}.  Not sure where that is.
And you have a #{computer} computer.  Nice.
"""

$stderr.puts $stdin.class