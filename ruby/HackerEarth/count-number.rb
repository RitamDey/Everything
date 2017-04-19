cases = $stdin.gets.chomp.to_i

for _ in 1..cases do
  _ = $stdin.gets

  puts $stdin.gets.chomp.scan(/[0-9]+/).size
end
