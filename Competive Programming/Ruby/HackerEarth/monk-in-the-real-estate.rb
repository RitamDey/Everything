require 'set'


def count_cities(n)
    cities = Set.new
    cities_count = 0

    n.times do |_|
        start_edge, end_edge = gets().split(' ').map(&:to_i)
        if !cities.include?(start_edge)
            cities_count += 1
            cities.add(start_edge)
        end

        if !cities.include?(end_edge)
            cities_count += 1
            cities.add(end_edge)
        end
    end

    return cities_count
end


if __FILE__ == $0
    cases = gets().to_i()

    cases.times do |_|
        puts(count_cities(gets().to_i()))
    end
end
