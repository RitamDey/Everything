class MegaGreeter
    # attr_accessor is a short hand for creating 
    # both getter and setter for in a class
    attr_accessor :names

    # Create the object
    def initialize(names = "World")
        @names = names
    end

    # Say hi to everybody
    def say_hi
        # Checks if the name attribute is nil or not
        if @names.nil?
            puts "..."
        
        # Check if the name attribute has a each method
        # If it does then it is a iterable
        elsif @names.respond_to?("each")
        # @names is a list of some kind, iterate!
            @names.each do |name|
                puts "Hello #{name}!"
            end
        else
            puts "Hello #{@names}!"
        end
    end

    # Say bye to everybody
    def say_bye
        if @names.nil?
            puts "..."
        
        # Check if the name attribute has a join method
        # If it does then it is a list
        elsif @names.respond_to?("join")
            # Join the list elements with commas
            puts "Goodbye #{@names.join(", ")}.  Come back soon!"
        else
            puts "Goodbye #{@names}.  Come back soon!"
        end
    end
end


# if __name__ == '__main__' but instead of using the current 
# namespace the match is done between the current 
# file name the running started and the file name (__FILE__) of this file
if __FILE__ == $0
    mg = MegaGreeter.new
    mg.say_hi
    mg.say_bye

    # Change name to be "Zeke"
    mg.names = "Zeke"
    mg.say_hi
    mg.say_bye

    # Change the name to an array of names
    mg.names = ["Albert", "Brenda", "Charles", "Dave", "Engelbert"]
    mg.say_hi
    mg.say_bye

    # Change to nil
    mg.names = nil
    mg.say_hi
    mg.say_bye
end