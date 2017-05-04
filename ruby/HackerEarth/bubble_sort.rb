len = $stdin.gets.strip.to_i
arr = $stdin.gets.strip.split.map { |n| n.to_i }
swaps = 0


for i in 0...(len-1)
    for j in 0...(len-1)
        if arr[j] > arr[j+1]
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
        end
    end
end


$stdout.puts swaps
