require 'HelloWorld'
puts 'Hello World'
puts "Program name #{$PROGRAM_NAME} in file #{$FILENAME}"

name = gets.chomp

puts "And Hello #{name}"

k = Hello.new
puts k.hello