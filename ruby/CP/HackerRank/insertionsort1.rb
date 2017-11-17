def insertion_sort(arr, len)
    e = arr[-1]
    y = len - 1

    while (y>0) && (arr[y-1] > e)
        arr[y] = arr[y-1]
        y -= 1
        puts arr.join(" ")
    end

    arr[y] = e
    puts arr.join(" ")
end


len = gets.chomp.to_i
arr = gets.chomp.split.map { |x| x.to_i }
insertion_sort(arr, len)
