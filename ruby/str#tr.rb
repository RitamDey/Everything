=begin
  Returns a copy of str with the characters in `from_str` replaced by the
  characters corresponding characters in `to_str`. If `to_str` is shorter than
  `from_str`, it is padded with its character in order to maintain the correspondence
=end

def rot13(messages)
  return messages.map { |msg| msg.tr('a-zA-Z', 'n-za-mN-ZA-M') }
end


if __FILE__ == $0
  print "Enter a line: "
  message = $stdin.gets.chomp.partition " "
  puts rot13(message)
end
