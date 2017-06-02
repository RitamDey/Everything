if __FILE__ == $0
    line_count = 0
    word_count = 0

    File.open("text.txt").each { |line| line_count += 1; word_count += line.length }

    $stdout.puts "Line Count is #{line_count}"
    $stdout.puts "Word Count is #{word_count}"
end
