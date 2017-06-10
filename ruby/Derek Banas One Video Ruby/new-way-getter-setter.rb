class Animal
    def initialize(name)
        @name = name
        @@type = "Animal"
        $stdout.puts "Creating #{@@type} #{@name}"
    end

    def name
        return @name
    end

    def name=(n)
        @name = n
    end

    def type
        return @@type
    end
end


dog = Animal.new("Jammy")
$stdout.puts "#{dog.name} is of type #{dog.type}"
$stdout.print "Enter a animal name: "

dog.name = $stdin.gets.chomp
begin
    $stdout.print "Enter a animal type: "
    dog.type = $stdin.gets.chomp
rescue
    $stdout.puts "Type can't be set"
end
$stdout.puts "#{dog.name} is of type #{dog.type}"
