len, rm_index = $stdin.gets().split().map { |x| x.to_i }
cost = $stdin.gets().split().map { |x| x.to_i }


b_charged = $stdin.gets().chomp().to_i()
b_actual = 0

0.upto(len-1) do |i|
    b_actual += cost[i] if i != rm_index
end

b_actual /= 2


if b_charged > b_actual
    $stdout.puts(b_charged - b_actual)
else
    $stdout.puts("Bon Appetit")
end
