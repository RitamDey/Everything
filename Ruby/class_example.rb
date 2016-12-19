=begin
This is a basic class declaration in Ruby
=end

class Car
    def start
        # This is a basic method declarationin Ruby
        puts("Bhrummm.....")
        # The `end` statment is used to end a block or 
        # method or class in Ruby
    end
    
    def price
        puts("Expensive")
    end
end

# <class name>.new is used to create a object in Ruby
Porshe = Car.new
# One way of calling function in Ruby
Porshe.price()
Porshe.start()

Nano = Car.new

# Over-ridding a particular method without inherting the class
# Also called Singleton class
def Nano.start
    puts("Phattt Phatttt....")
end

def Nano.price
    puts("Extra Cheap")
end

# Other way of calling a function or method in Ruby
# Mainly used when the function or method doesn't require a parameter
Nano.price
Nano.start