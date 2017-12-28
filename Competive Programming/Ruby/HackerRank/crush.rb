def apply_op(array, start, end_index, adder)
    array[start-1,end_index] = array[start-1,end_index].map { |x| x+adder }
    return array
end


len, ops = gets().split().map(&:to_i)
array = [0]*len


1.upto(ops) do |_|
    start, end_index, adder = gets().split().map(&:to_i)
    array = apply_op(array, start, end_index, adder)
    puts(array)
end

#puts(array.max())
