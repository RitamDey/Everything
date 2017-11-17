len = gets().chomp().to_i()
count = 0
chocs = gets().chomp().split().map(&:to_i)
n_sums, n_parts = gets.chomp().split().map(&:to_i)


0.upto(len-1) do |i|
    if chocs[i...i+n_parts].sum() == n_sums
        count += 1
    end
end


puts(count)
