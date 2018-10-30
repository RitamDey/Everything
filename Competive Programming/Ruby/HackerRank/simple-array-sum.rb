def simpleArraySum(arr)
    sum = 0

    arr.each { |n| sum += n }

    return sum
end


if __FILE__ == $0
    arr_count = gets().to_i()

    arr = gets().split(" ").map(&:to_i)

    puts(simpleArraySum(arr))
end
