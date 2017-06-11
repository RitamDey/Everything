class Menu
    include Enumerable

    def each
        yield "Pizza"
        yield "Spaghetti"
        yield "Salad"
        yield "Water"
        yield "Bread"
    end
end


menu = Menu.new
menu.each do |item|
    puts "Do you want #{item} ?"
end


# Some general selection and finding operations can be done in enumerable class
$stdout.puts "\nFinding pizza: #{ menu.find { |item| item = "pizza" } }\n"
$stdout.puts "Selecting some: #{ menu.select { |item| item.size <= 5 } }\n"
$stdout.puts "Rejecting some: #{ menu.reject { |item| item.size <= 5 } }\n"

$stdout.puts "The first one is #{menu.first}\n"

$stdout.puts "taking only two: #{menu.take(2)}\n"  # Print first two
$stdout.puts "Dropping two: #{menu.drop(2)}\n" # Except first two
$stdout.puts "The maximum is #{menu.min}"
$stdout.puts "The minimum is #{menu.max}"
$stdout.puts "The sorted menu is #{menu.sort}"
menu.reverse_each { |item| $stdout.puts item } # Exceute the proc with reverse order
