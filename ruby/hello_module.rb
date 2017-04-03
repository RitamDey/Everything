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


    def say_hello(name)
        return "Hello #{name}"
    end
end
