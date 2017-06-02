if __FILE__ == $0
    line_count = 0
    text = ""

    File.open("text.txt").each do |line|
        line_count += 1
        text << 1
    end

    $stdout.puts "Line Count is #{line_count}"
end
