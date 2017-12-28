def insertion_sort(arr, len)
    1.upto(len-1) do |x|
        e = arr[x]
        y = x
        
        while (y>0) && (arr[y-1] > e)
            arr[y] = arr[y-1]
            y -= 1
        end
        
        arr[y] = e
        puts arr.join(" ")
    end
end


len = gets.chomp.to_i
arr = gets.chomp.split.map { |x| x.to_i }
insertion_sort(arr, len)
