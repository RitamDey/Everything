def getRecord(arr, length)
    high = low = arr[0]
    high_count = low_count = 0

    for score in arr.slice!(1, length)
        if score > high
            high_count += 1
            high = score
        end

        if score < low
            low_count += 1
            low = score
        end
    end

    return high_count, low_count
end


length = $stdin.gets().chomp().to_i
arr = $stdin.gets().chomp().split().map! { |x| x.to_i }
result = getRecord(arr, length)
$stdout.puts(result.join(" "))
