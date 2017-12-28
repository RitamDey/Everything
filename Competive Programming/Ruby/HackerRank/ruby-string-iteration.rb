=begin
It's a method only submission. I don't know other details
=end


def count_multibyte_char(str)
    count = 0  # Counter to hold the number of chars

    str.each_char { |char|
        # The bytes return a array representing the bytes 
        # used to represent the character
        if char.bytes.length > 1
            count += 1
        end
    }

    return count
end
