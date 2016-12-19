# Variable declaration in Ruby is same as Python and PHP

some_var = 10
puts some_var

=begin
Constants are declared using Variables with upper case first char
They are totally Constants like that in Java or C and can be reassigned
But doing so Ruby gives a warning and does it anyway
For this code the warning is: 
variables.rb:12: warning: already initialized constant ConstVar
variables.rb:10: warning: previous definition of ConstVar was here
=end

ConstVar = 11
puts ConstVar
ConstVar = 12
puts ConstVar
