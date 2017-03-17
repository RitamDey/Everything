def adder(a,b)
  return a+b
end

def multiply(a,b)
  a*b
end

def cover(func, a,b)
  puts func(a,b)
end

2.times do |a|
  x = gets.chomp.to_i
  y = gets.chomp.to_i
  if a==1
    puts adder(x,y)
  else
    puts multiply(x,y)
    # puts cover(multiply, x,y)
  end
end
