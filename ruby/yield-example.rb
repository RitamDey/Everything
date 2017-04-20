def intro(name)
    yield name
    yield "Amanda"
    yield name
    yield "John"
end

intro("sTux") { |name| puts "Hello, #{name}" }
