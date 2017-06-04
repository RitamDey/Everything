if __FILE__ == $0
    line_count = 0
    letter_count = 0
    letter_without_spaces = 0
    word_count = 0
    sentence_count = 0

    File.open("text.txt").each do |line|
        line_count += 1
        letter_count += line.length
        letter_without_spaces += line.gsub(/\s+/, '').length
        word_count += line.split.length
        sentence_count += line.split(/\.|\?|!/).length
    end

    $stdout.puts "Line Count is #{line_count}"
    $stdout.puts "Total characters present are #{letter_count}"
    $stdout.puts "Letter count without spaces are #{letter_without_spaces}"
    $stdout.puts "Word count are #{word_count}"
    $stdout.puts "Sentence count are #{sentence_count}"
    $stdout.puts "Words per Sentence are #{word_count/sentence_count}"
end
