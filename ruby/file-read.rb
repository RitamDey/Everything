filename = $stdin.gets.chomp!

txt = open(filename)  # We can python like open method
txt.close


txt = File.open(filename)  # Or use the File class

puts "Here's the your #{filename} content:"


puts txt.read


txt.close
