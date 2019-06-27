=begin
    Just a hello world method with 
    different argument list
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
hi "Joe Green"


def hi(name="sTux")
    puts "Hello #{name.capitalize}"
end


hi
hi("Joey")