def fact(n)
    return n*fact(n-1) unless n <= 0
    return 1
end


if __FILE__ == $0
	num = gets.chomp.to_i
	puts fact(num)
end

