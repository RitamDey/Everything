def power(n)
  if n == 0
    return 1
  end

  res = power(n/2)

  if n%2 == 0
    return res * res
  else
    return res * res * 3
  end
end


if __FILE__ == $0
  n = gets().chomp().to_i()

  puts(power(n))
end
