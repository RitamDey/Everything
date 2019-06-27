=begin
Lazy evaluation is an evaluation strategy that delays the assessment of an expression until its value is needed. 

The example is taken from HackerRank.
Here:
https://en.wikipedia.org/wiki/Lazy_evaluation
https://www.hackerrank.com/challenges/ruby-lazy
=end


power_array = -> (power, array_size) do
    1.upto(Float::INFINITY).lazy.map { |x| x**power }.first(array_size)
end


puts "[#{power_array.(2, 4).join(", ")}]"
puts "[#{power_array.(3, 5).join(", ")}]"
