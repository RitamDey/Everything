=begin
This solution works for Case 1, 3 and 4. The case 2 always gets timedout
=end


value = gets.chomp.to_i
high = gets.chomp.to_i - 1
arr = gets.chomp.split(" ").map { |x| x.to_i }
low = 0


while true
    mid = (high-low)/2

    puts "High #{high} Low #{low} Middle #{mid}"
    if value > arr[mid]
        low = mid
    elsif value < arr[mid]
        high = mid
    else
        puts mid
        break
    end
end
