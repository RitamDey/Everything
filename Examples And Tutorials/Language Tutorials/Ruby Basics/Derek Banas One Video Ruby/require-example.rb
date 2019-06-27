require_relative "human-module"
require_relative "smart-module"


module Animal
    def make_sound
        puts "Grr"
    end
end


class Dog
    include Animal
end

rover = Dog.new
rover.make_sound

class Scientist
    include Human
    prepend Smart

    def act_smart
        return "E = mc^2"
    end
end

einstein = Scientist.new
einstein.name = "Albert"

$stdout.puts einstein.name
$stdout.puts einstein.name + " says "+einstein.act_smart
