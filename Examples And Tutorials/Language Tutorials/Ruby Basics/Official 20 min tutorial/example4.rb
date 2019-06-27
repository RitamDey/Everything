=begin
    Class example
=end


class Greeter
    attr_accessor :name
    attr_writer :name

    def initialize(name = "World")
        @name = name
    end

    def say_hi
        puts "Hello #{@name}!"
    end

    def say_bye
        puts "Bye #{@name}!"
    end
end

obj = Greeter.new()
obj.say_hi
obj.say_bye()

obj = Greeter.new("sTux")
obj.say_hi
obj.say_bye()
