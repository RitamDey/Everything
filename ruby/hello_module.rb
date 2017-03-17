module Person
    class Persion
        def initialize(name, sex)
            @name = name
            @sex = sex
        end

        def hello()
            puts "Hello #{@name}"
        end

        def get_sex()
            return "Sex #{@sex}"
        end
    end
end

module Hello
    def say_hello(name)
        return "Hello, #{name}"
    end
end


import Hello
import Person

puts Hello.say_hello("sTux")

obj = Person.Person.new("sTux", "Male")
puts obj.get_sex
puts obj.hello()
