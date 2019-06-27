x = 1


loop do
    x += 1

    next unless x%2 == 0

    break unless x<=10

    $stdout.puts x
end
