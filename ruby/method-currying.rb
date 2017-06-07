=begin

Defination of method currying
In mathematics and computer science,
currying is the technique of translating the evaluation of a function that
takes multiple arguments (or a tuple of arguments) into evaluating
a sequence of functions, each with a single argument
=end


multiply_numbers = -> (x, y) do
    return x*y
end


doubler = multiply_numbers.curry.(2)
tripler = multiply_numbers.curry.(3)


puts doubler.(4)
puts tripler.(4)
