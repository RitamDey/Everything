_ = gets().to_i()
arr_orig = gets().split().map(&:to_i)
arr = arr_orig.clone()


1.upto(arr.length-1) do |i|
  key = arr[i]
  j = i - 1

  while j >= 0 && arr[j] > key
    arr[j+1] = arr[j]
    j -= 1
  end
  # When we reach here, the element `j` is pointing to
  # is smaller than `key`. So we insert to maintain the
  # sorted nature of the subarray, we insert `key` at `j+1`
  arr[j+1] = key
end


puts arr.join(" ")
for elem in arr
  print "#{arr_orig.index(elem) + 1} "
end
puts
