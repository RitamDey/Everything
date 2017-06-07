$stdout.print "Enter your age: "
age = $stdin.gets.to_i

$stdout.print "Enter the recommened age: "
rec = $stdin.gets.to_i

=begin
The `<=>` operator is used to compare two values for `<` `>` and `=`.

-1 is returned if the first argument is less than the second one.
1 is returned if the second argument is more than the second one.
0 is returned if both arguments are same
=end
res = age <=> rec

if (res == 0)
    $stdout.puts "You're okay"

elsif (res == 1)
    $stdout.puts "Cool!. You are good!"

elsif (res == -1)
    $stdout.puts "You are a kiddo!"
end

$stdout.puts "#{age} <=> #{rec} = #{res}"
