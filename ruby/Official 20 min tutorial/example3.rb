=begin
    Just a hello world method
rescue => exception
    
=end

def hi
    puts "Hello World"
end


hi
hi()


def hi(name)
    puts "Hello #{name.capitalize}"
end


hi("sTux")
hi("Joe Green")